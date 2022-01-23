import osmloading.osm as osm
osm.scale = 100
import base.gfx as gfx
import time
import systems.navigation.newnav as nav
import osmloading.new_intersections as inters_new
import random
import systems.m2D.draw_property as drawprop2d

#Plan
#refactor: intersection with building/street/etc, nav seperate
    # utilities: graphics
    # osm: osm, properties, intersections
    # systems: gps, range finder, modelling
    # tests
#algorithim for location (quickly see if object is within range)
#Get locations for building objs (osm wiki)
#put gps object in a dict


#Done????
#spread out the 10th updates, rn it does it the first 10th
#Program updates every X
#Sub updates can happen every X/Y
    #Y is the interval
#fix scaling lmao

gfx.setup_gfx()

updatePerSec = 60
tenth = updatePerSec/10
half = updatePerSec/2
currupdate = 1

class bike():
    def __init__(self,origin,end):
        self.origin = origin
        self.end = end
        self.getroute(origin,end)
        self.pos = [0,0,0]
        self.cube = gfx.cube()
        gfx.gfx_cubes.append(self.cube)
    def getroute(self,origin,end):
        self.gps = nav.gps(origin)
        lengths = inters_new.lengths
        thegraph = inters_new.graph
        self.gps.process()
        self.road2go = self.gps.getnodes(end)
        self.count = 0
    def loop(self):
        if(self.count >= len(self.road2go)):
            self.origin = self.end
            #Randomly generate a new destination
            possible_dests = list(inters_new.graph.keys())
            chosen_dest = random.randint(0,len(possible_dests)-1)
            self.end = possible_dests[chosen_dest]
            self.getroute(self.origin,self.end)
            while (len(self.road2go) <= 0):
                #Randomly generate a new destination
                possible_dests = list(inters_new.graph.keys())
                chosen_dest = random.randint(0,len(possible_dests)-1)
                self.end = possible_dests[chosen_dest]
                self.getroute(self.origin,self.end)
            # print(self.road2go)
            None
        else:
            #Current node
            node = self.road2go[self.count]
            cord =osm.nodetocords(node)
            self.pos = osm.getpont(cord)
            self.cube.setpos(self.pos[0],0,self.pos[1])
            self.count += 1

drawprop2d.draw_roads()

tenths = []
limit = False
while not gfx.rl.window_should_close():
    b4 = time.time()

    #Keep program updating every X
    currupdate += 1
    gfx.loop()
    if(currupdate%tenth == 0):
        max = 2
        count = 0
        for workingbike in tenths:
            if(count > max):
                break
            count += 1
            tenths.remove(workingbike)
            workingbike.loop()
            tenths.append(workingbike)
    if(currupdate%half == 0):
        None
        # print(str(currupdate)+"every half??")
    if(currupdate == 60):
        if(not limit):
            tenths.append(bike(97247821,340162270))
        # print("every sec")
        currupdate = 1
    after = time.time()
    # print("Frame time: "+str((after-b4)))
    if((after-b4)>0.05):
        print("LAG at " + str(len(tenths)))
        # gfx.quit_gfx()
        # break


gfx.quit_gfx()