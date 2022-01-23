import base.gfx as gfx
import systems.m3D.street_gen as sgen


gfx.setup_gfx()
gfx.load_streets()

while not gfx.rl.window_should_close():
    try:
        gfx.loop()
    except KeyboardInterrupt:
        break
gfx.quit_gfx()