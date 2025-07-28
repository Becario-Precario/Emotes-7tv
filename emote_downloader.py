#!/usr/bin/env python3
import requests
import os
import re
import argparse
from PIL import Image
from io import BytesIO

def limpiar_nombre(nombre):
    """Reemplaza caracteres inválidos en nombres de archivo de Windows."""
    return re.sub(r'[\\/*?:"<>|]', "_", nombre)

def descargar_emotes(set_id, output_dir, format_priority):
    """Descarga emotes desde un set de 7TV según formato de prioridad."""
    # Preparar directorios y archivo de errores
    os.makedirs(output_dir, exist_ok=True)
    error_log = os.path.join(output_dir, "errores.txt")
    if os.path.exists(error_log):
        os.remove(error_log)

    descargados = 0
    fallidos = 0

    # Llamada a API
    url = f"https://7tv.io/v3/emote-sets/{set_id}"
    resp = requests.get(url)
    if resp.status_code != 200:
        print(f"Error: no se pudo acceder al set {set_id} (HTTP {resp.status_code})")
        return

    data = resp.json()
    for emote in data.get("emotes", []):
        nombre_orig = emote.get("name", "sin_nombre")
        nombre = limpiar_nombre(nombre_orig)
        host = emote.get("data", {}).get("host", {})
        base_url = host.get("url")
        archivos = host.get("files", [])
        if not base_url or not archivos:
            with open(error_log, "a", encoding="utf-8") as f:
                f.write(f"{nombre_orig} -> sin archivos disponibles\n")
            fallidos += 1
            continue

        # buscar archivo por prioridad
        elegido = None
        for fmt in format_priority:
            elegido = next((f for f in archivos if f["name"].endswith(f"4x.{fmt}")), None)
            if elegido:
                break
        if not elegido:
            with open(error_log, "a", encoding="utf-8") as f:
                f.write(f"{nombre_orig} -> formatos no encontrados: {', '.join(format_priority)}\n")
            fallidos += 1
            continue

        full_url = f"https:{base_url}/{elegido['name']}"
        out_path = os.path.join(output_dir, f"{nombre}.{elegido['format'].lower()}")

        try:
            img_data = requests.get(full_url).content
            if elegido["format"].lower() == "gif":
                with open(out_path, "wb") as f:
                    f.write(img_data)
            else:
                img = Image.open(BytesIO(img_data)).convert("RGBA")
                img.save(out_path, format=elegido["format"].upper())
            descargados += 1
            print(f"✔️ {nombre_orig} -> {elegido['format']} descargado")
        except Exception as e:
            with open(error_log, "a", encoding="utf-8") as f:
                f.write(f"{nombre_orig} -> Error: {e}\n")
            print(f"❌ Error {nombre_orig}: {e}")
            fallidos += 1

    # Resumen
    print(f"\n✅ Descargados: {descargados}")
    print(f"❌ Fallidos: {fallidos}")
    if fallidos:
        print(f"📄 Revisa {error_log} para detalles")

def main():
    parser = argparse.ArgumentParser(description="Descarga emotes desde un set de 7TV")
    parser.add_argument("--set", "-s", required=True, help="ID del set de emotes en 7TV")
    parser.add_argument("--out", "-o", default="emotes_7tv", help="Carpeta de salida")
    parser.add_argument("--formats", "-f", default="gif,webp,avif",
                        help="Formatos por prioridad, separados por comas")
    args = parser.parse_args()

    fmt_list = [fmt.strip() for fmt in args.formats.split(",")]
    descargar_emotes(args.set, args.out, fmt_list)

if __name__ == "__main__":
    main()
