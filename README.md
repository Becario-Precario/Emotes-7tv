# 🧠 7TV Emote Downloader

Este es un script en Python que descarga todos los emotes de un set de [7TV](https://7tv.app) en el formato más óptimo disponible (`GIF`, `WEBP`, o `AVIF`). Está pensado para que funcione de forma robusta, detectando errores, limpiando nombres inválidos en Windows, y priorizando calidad.

---

## ✅ Características

- Descarga automática de todos los emotes de un set dado.
- Soporte para múltiples formatos: `GIF`, `WEBP`, `AVIF`.
- Limpieza de nombres ilegales en Windows (`?`, `*`, `:`...).
- Registro de errores en un archivo `errores.txt`.
- Control de resolución: se prioriza la calidad `4x` si existe.
- Código limpio, comentado y mantenible.

---

## 🚀 Requisitos

Antes de ejecutar, asegúrate de tener Python 3 y estas dependencias:

```bash
pip install requests pillow
```

También puedes instalar `imageio` si en un futuro se añade soporte para `.webp` animado → `.gif`:

```bash
pip install imageio[ffmpeg]
```

---

## 🛠 Cómo usarlo

1. Clona este repositorio o descarga el archivo `emote_downloader.py`.
2. Abre una terminal en la carpeta del script.
3. Ejecuta el script con Python:

```bash
python emote_downloader.py
```

Los emotes se guardarán por defecto en la carpeta `emotes_7tv`.

---

## 📝 Configuración

En la parte superior del script puedes ajustar:

```python
emote_set_id = "ID_DEL_SET"
output_dir = "emotes_7tv"
format_priority = ["gif", "webp", "avif"]
```

- **`emote_set_id`**: ID del set de 7TV que quieres descargar (puedes copiarlo desde la URL). https://7tv.app/emote-sets/**01HXVFJ9PR000BMH9V93EWGVFC**
- **`output_dir`**: Carpeta donde se guardarán los emotes.
- **`format_priority`**: Orden de preferencia de formatos (puedes dejar solo uno si lo deseas).

---

## 🧾 Registro de errores

Si algún emote falla al descargarse, se guardará una entrada en `errores.txt` con el nombre del emote y el motivo:

```text
Nails → Ningún formato disponible (gif, webp, avif)
dafuq? → Error: [Errno 22] Invalid argument: 'emotes_7tv\dafuq?.gif'
```

---

## 🤖 Créditos

Desarrollado por [@JoanBeltran](https://github.com/JoanBeltran) con asistencia técnica de [ChatGPT](https://openai.com/chatgpt).

Gracias a ChatGPT por el soporte técnico, generación del código, control de errores y optimización del script.
