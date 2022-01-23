import systems.m2D.draw_property as dr
import base.gfx as gfx

gfx.setup_gfx()
dr.draw_buildings()
count = 0
while True:
    try:
        gfx.loop()
    except KeyboardInterrupt:
        break
gfx.quit_gfx()
