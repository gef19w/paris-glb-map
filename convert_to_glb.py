import bpy

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.obj(filepath='paris.obj')
bpy.ops.export_scene.gltf(filepath='paris.glb', export_format='GLB')
bpy.ops.wm.quit_blender()
