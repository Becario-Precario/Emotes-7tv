# 🧠 7TV Emote Downloader

Script en Python para descargar todos los emotes de un set de [7TV](https://7tv.app) en el formato más óptimo (`GIF`, `WEBP`, `AVIF`). Maneja errores, limpia nombres inválidos y prioriza calidad.

---

## 🚀 Requisitos

* **Python 3.7+**
* Instala dependencias con:

  ```bash
  pip install -r requirements.txt
  ```

---

## 🛠 Uso (CLI)

Ejecuta desde la terminal en la carpeta del proyecto:

```bash
python emote_downloader.py \
  --set 01HXVFJ9PR000BM9V93EWGVFC \
  --out emotes_7tv \
  --formats gif,webp,avif
```

Parámetros:

* `--set` (`-s`): ID del set de emotes en 7TV (p. ej. `01HXVFJ9PR000BM9V93EWGVFC`).
* `--out` (`-o`): Carpeta donde se guardarán los emotes. Por defecto `emotes_7tv`.
* `--formats` (`-f`): Formatos por prioridad, separados por comas. Por defecto `gif,webp,avif`.

---

## 📊 Ejemplo de salida

```bash
$ python emote_downloader.py -s 01HXVFJ9PR000BM9V93EWGVFC -o emotes -f gif,webp,avif
✔️ PETTHEMODS -> GIF descargado
✔️ peepoRiot -> WEBP descargado
…
✅ Descargados: 926
❌ Fallidos: 0
```

---

## 📝 Configuración

Puedes ajustar variables directamente en CLI o modificar:

```python
# En emote_downloader.py
# format_priority = ["gif", "webp", "avif"]
```

---

## 🧾 Registro de errores

Si algún emote falla, se guarda en `errores.txt` dentro de la carpeta de salida:

```text
Nails -> formatos no encontrados: gif, webp, avif
dafuq? -> Error: [Errno 22] Invalid argument
```

---

## 🤖 Créditos

Desarrollado por [@JoanBeltran](https://github.com/Becario-Precario) con asistencia técnica de [ChatGPT](https://openai.com/chatgpt).

Gracias a ChatGPT por el soporte técnico, generación del código, control de errores y optimización del script.

---

## 📄 Licencia

MIT License.
