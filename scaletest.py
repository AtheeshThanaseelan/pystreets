import base.gfx as gfx
# import m3D.street_gen as sgen
# import m3D.building_gen as bgen

gfx.setup_gfx()
# gfx.load_streets()
# bgen.make_all()
# gfx.load_buildings()
cube = gfx.cube()
# cube.setpos(10,0.5,10)



gfx.gfx_cubes.append(cube)
while not gfx.rl.window_should_close():
    try:
        gfx.loop()
    except KeyboardInterrupt:
        break
gfx.quit_gfx()