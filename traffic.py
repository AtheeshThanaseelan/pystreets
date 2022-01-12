from navigation.newnav import *

#Know the update increments


class bike():
    def __init__(self,x,y,z):
        self.pos = [x,y,z]
        self.repgfx = gfx.cube()
        self.repgfx.setpos(x,y,z)
    


test = gps(97247821)
test.process(thegraph,lengths)
road2go = test.getnodes(340162270)


gfx.setup_gfx()
drawprop.draw_roads()
bike = gfx.cube()
gfx.gfx_cubes.append(bike)

while not gfx.rl.window_should_close():
    count = 0
    for node in road2go:
        while(count<100):
            count += 1
        gfx.loop()
        tools2d.nodetocube(node,1,bike)
    gfx.loop()

gfx.quit_gfx()

