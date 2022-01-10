import base.gfx as gfx

gfx.setup_gfx()
gfx.load_streets()

while True:
    try:
        gfx.loop()
    except KeyboardInterrupt:
        break
gfx.quit_gfx()