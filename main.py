import os

# تحميل خريطة باريس
os.system("wget -O paris.osm.pbf http://download.geofabrik.de/europe/france/ile-de-france-latest.osm.pbf")

# تحميل Osm2World.jar
os.system("wget -O Osm2World.jar https://github.com/tordanik/Osm2World/releases/latest/download/Osm2World.jar")

# تحويل إلى OBJ
os.system("java -jar Osm2World.jar paris.osm.pbf -o paris.obj")

# إنشاء سكربت Blender للتحويل إلى GLB
with open('convert_to_glb.py', 'w') as f:
    f.write("""import bpy

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.obj(filepath='paris.obj')
bpy.ops.export_scene.gltf(filepath='paris.glb', export_format='GLB')
bpy.ops.wm.quit_blender()
""")

# تنفيذ التحويل عبر Blender
os.system("blender -b -P convert_to_glb.py")
