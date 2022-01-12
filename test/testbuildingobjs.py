import base.gfx as gfx

gfx.setup_gfx()
gfx.load_buildings()

while not gfx.rl.window_should_close():
    try:
        gfx.loop()
    except KeyboardInterrupt:
        break
gfx.quit_gfx()