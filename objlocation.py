import osmloading.osm

osmloading.osm.scale = 1000

import systems.m3D.building_gen as building_gen
import systems.m2D.draw_property as prop2d
import base.newgfx as gfx
import os
import pickle

loopframe = gfx.gfxframe()
# prop2d.draw_buildings()
# loopframe.custom_funcs.append(gfx.gfxlineupdate)

bid = 31363791
new = True
if(new):
    # building_gen.obj_and_locs(bid)
    # building_gen.make_all_new()
    gfx.loadmodelloc()
    loopframe.custom_funcs.append(gfx.gfxlocmodelupdate)
    loopframe.custom_funcs.append(gfx.camgrid)
else:
    building_gen.make_building_obj(bid)
    gfx.load_buildings()
    loopframe.custom_funcs.append(gfx.gfxmodelupdate)



while loopframe.loop():
    pass


