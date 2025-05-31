# 🖼️ Blender Auto-Thumbnail Generator

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white&style=flat-square)
![Blender](https://img.shields.io/badge/Blender-4.4-orange?logo=blender)
![License](https://img.shields.io/badge/License-MIT-green)

**Script to automatically generate thumbnails when saving Blender files**

## 📝 Description

This Blender script automatically generates a PNG thumbnail every time you save your `.blend` file. The thumbnail is saved in the same location as the original file with the `_thumb.png` suffix.

## ✨ Features

- Automatic thumbnail generation on save
- Configurable size (800×600px by default)
- High-quality PNG format (or another formats)
- Original settings restoration
- Built-in error handling

## 🛠️ Requirements

- Blender 4.4+
- Python 3.11 (included in Blender)

## 🚀 Installation

Option 1

Paste the code in the text editor panel within the .blend file where you want to use this feature (for example, in the default startup file).
You need to enable script execution in Blender's preferences and reload the file each time you modify the script.

Option 2

Save as `auto_thumbnail.py` in your scripts folder: