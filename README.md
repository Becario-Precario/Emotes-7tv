# 7TV Emote Downloader

Este es un script en Python que descarga todos los emotes de un set de [7TV](https://7tv.app) en el formato más óptimo disponible (`GIF`, `WEBP`, o `AVIF`). Está pensado para que funcione de forma robusta, detectando errores, limpiando nombres inválidos en Windows, y priorizando calidad.

---

## Características

- Descarga automática de todos los emotes de un set dado.
- Soporte para múltiples formatos: `GIF`, `WEBP`, `AVIF`.
- Limpieza de nombres ilegales en Windows (`?`, `*`, `:`...).
- Registro de errores en un archivo `errores.txt`.
- Control de resolución: se prioriza la calidad `4x` si existe.
- Código limpio, comentado y mantenible.

---

## Requisitos

Antes de ejecutar, asegúrate de tener Python 3 y estas dependencias:

```bash
pip install requests pillow
