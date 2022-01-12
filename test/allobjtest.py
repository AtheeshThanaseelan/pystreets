import base.gfx as gfx
import m3D.street_gen as sgen
import m3D.building_gen as bgen

gfx.setup_gfx()
gfx.load_streets()
gfx.load_buildings()
while not gfx.rl.window_should_close():
    try:
        gfx.loop()
    except KeyboardInterrupt:
        break
gfx.quit_gfx()