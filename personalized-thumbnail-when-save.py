import bpy
import os

def save_thumbnail(scene):
    """Guarda miniatura automáticamente al guardar el archivo"""
    try:
        if not bpy.data.filepath:
            return
        
        # 1. CAPTURAR la configuración actual ANTES de cambiar nada
        original_res_x = bpy.context.scene.render.resolution_x
        original_res_y = bpy.context.scene.render.resolution_y
        original_percentage = bpy.context.scene.render.resolution_percentage

        output_path = bpy.data.filepath.replace(".blend", "_thumb.png")
        bpy.context.scene.render.image_settings.file_format = 'PNG'
        bpy.context.scene.render.resolution_x = 800
        bpy.context.scene.render.resolution_y = 600
        bpy.context.scene.render.resolution_percentage = 100
        
        bpy.ops.render.opengl(view_context=True)
        bpy.data.images['Render Result'].save_render(filepath=output_path)
        
        bpy.context.scene.render.resolution_x = original_res_x
        bpy.context.scene.render.resolution_y = original_res_y
        bpy.context.scene.render.resolution_percentage = original_percentage
        
    except Exception as e:
        print(f"Error en auto-thumbnail: {e}")

# Registrar el handler
bpy.app.handlers.save_post.append(save_thumbnail)
print("✅ Auto-Thumbnail activado (sin interfaz)")