# 🖼️ Blender Auto-Thumbnail Generator

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white&style=flat-square)
![Blender](https://img.shields.io/badge/Blender-4.4-orange?logo=blender)
![License](https://img.shields.io/badge/License-MIT-green)

**Script para generar miniaturas automáticamente al guardar archivos en Blender**

## 📝 Descripción

Este script para Blender genera automáticamente una miniatura en formato PNG cada vez que guardas tu archivo `.blend`. La miniatura se guarda en la misma ubicación que el archivo original con el sufijo `_thumb.png`.

## ✨ Características

- Generación automática de miniaturas al guardar
- Tamaño configurable (800×600px por defecto)
- Formato PNG de alta calidad
- Restauración de configuraciones originales
- Manejo de errores integrado

## 🛠️ Requisitos

- Blender 4.4+
- Python 3.11 (incluido en Blender)

## 🚀 Instalación

opcion 1

Pegar el codigo en el panel de texto en el archivo blend donde se quiera utilizar esta caracteristica, por ejemplo en el archivo de inicio por defecto.
Es necesario permitir en configuracion de blender la ejecucion de scripts y recargar el archivo cada vez que se modifique el script

opcion 2

Guarda como `auto_thumbnail.py` en tu carpeta de scripts: