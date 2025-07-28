import requests
import os
import re
from PIL import Image
from io import BytesIO

# Configuración
emote_set_id = "ID_DEL_SET"
output_dir = "emotes_7tv"
error_log_path = "errores.txt"
format_priority = ["gif", "webp", "avif"]

# Preparar entorno
os.makedirs(output_dir, exist_ok=True)
if os.path.exists(error_log_path):
    os.remove(error_log_path)

# Función para limpiar nombres de archivo
def limpiar_nombre(nombre):
    return re.sub(r'[\\/*?:"<>|]', "_", nombre)

# Inicializar contadores
descargados = 0
fallidos = 0

# Descargar set
url = f"https://7tv.io/v3/emote-sets/{emote_set_id}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    for emote in data["emotes"]:
        nombre_original = emote.get("name", "emote_sin_nombre")
        nombre = limpiar_nombre(nombre_original)
        host = emote.get("data", {}).get("host", {})
        base_url = host.get("url")
        archivos = host.get("files", [])

        if not base_url or not archivos:
            with open(error_log_path, "a", encoding="utf-8") as log:
                log.write(f"{nombre_original} → Sin archivos disponibles\n")
            fallidos += 1
            continue

        archivo_encontrado = None
        for formato in format_priority:
            archivo_encontrado = next(
                (f for f in archivos if f["name"].endswith(f"4x.{formato}")), None)
            if archivo_encontrado:
                break

        if not archivo_encontrado:
            with open(error_log_path, "a", encoding="utf-8") as log:
                log.write(f"{nombre_original} → Ningún formato disponible ({', '.join(format_priority)})\n")
            fallidos += 1
            continue

        # Construir URL
        url_completa = f"https:{base_url}/{archivo_encontrado['name']}"
        ruta = os.path.join(output_dir, f"{nombre}.{archivo_encontrado['format'].lower()}")

        try:
            img_data = requests.get(url_completa).content
            if archivo_encontrado["format"].lower() == "gif":
                with open(ruta, "wb") as f:
                    f.write(img_data)
                print(f"🎞️ {nombre} → GIF descargado")
            else:
                img = Image.open(BytesIO(img_data)).convert("RGBA")
                img.save(ruta, format=archivo_encontrado["format"].upper())
                print(f"🖼️ {nombre} → convertido a {archivo_encontrado['format'].upper()}")
            descargados += 1
        except Exception as e:
            with open(error_log_path, "a", encoding="utf-8") as log:
                log.write(f"{nombre_original} → Error: {str(e)}\n")
            print(f"❌ Error con '{nombre_original}': {e}")
            fallidos += 1
else:
    print("❌ Error al acceder a la API:", response.status_code)

# Resumen
print("\n🔚 Proceso completado.")
print(f"✔️ Emotes descargados correctamente: {descargados}")
print(f"❌ Emotes fallidos: {fallidos}")
if fallidos > 0:
    print(f"📄 Revisa el archivo '{error_log_path}' para ver detalles.")
