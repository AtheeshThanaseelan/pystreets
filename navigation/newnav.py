import base.osm as osm
import base.properties as sts
import base.gfx as gfx
import m2D.tools as tools2d
import navigation.traverse as trav

import navigation.getIntersections as inters_orig
import navigation.new_intersections as inters_new

import m2D.draw_property as drawprop
import math #as math

import copy

wayids = sts.roads
ways = osm.df_ways
intersections = inters_new.intersections
lengths = inters_new.lengths
thegraph = inters_new.graph

# Nav.py
#heap for djistra
#length of each road(way)
#make a graph with the connecting nodes + length of the roads
#djistra algorithim
#Store closest intersections found with algorithim using paths = {}


#Our heap representation
class bootlegheap:
    def __init__(self):
        self.heapRep={}
        self.done = {}
    def add(self,num,weight):
        self.heapRep.update({num:weight})
        self.done.update({num:0})
    def visited(self,num):
        self.done.update({num:1})
        #self.heapRep.pop(num)
    def getdist(self,num):
        return self.heapRep[num]
    def getmin(self):
        lowest = float('inf')
        for n in self.heapRep:
            if((self.heapRep[n] < lowest)&(self.done[n]==0)):
                lowest = self.heapRep[n]
        for n in self.heapRep:
            if(lowest == self.heapRep[n]):
                return n
        return None
    def print(self):
        for x in self.heapRep:
            print(x,self.heapRep[x])

class gps():
    def __init__(self,initial_node):
        self.inital_node = initial_node
    def process(self,thegraph,lengths):
        ##Holding paths (node to node)
        self.path = {}
        path = self.path
        graph = copy.copy(thegraph)
        ##Run djistakara 
        heap = bootlegheap()
        start = self.inital_node#97247821
        heap.add(start,0)
        for inter in graph:
            if(inter != start):
                heap.add(inter,float('inf'))
        quit = 0
        curr = (heap.getmin())
        while (quit == 0):
            curdists = graph[curr]
            for point in curdists:
                try:
                    dist = heap.getdist(point)
                    newdist = heap.getdist(curr) + curdists[point]
                    if(newdist < dist):
                        heap.add(point,newdist)
                        path.update({point:curr})
                except:
                    print("missing node")
            ##After all are checked, mark as visited and move on
            graph.pop(curr)
            heap.visited(curr)
            ##Next node will be the node with the smallest tentative distance
            curr = (heap.getmin())
            #print("next:" + str(curr))
            ##If the next node has either already been visted or the distance is inf, STOP
            try:
                graph[curr]
            except:
                print("except")
                quit = 1
            if(heap.getdist(curr) == float('inf')):
                quit = 1
    def getnodes(self,destination):
        #Get the path (node to node)
        ex_dest = destination#340162270#97247995#97247887
        origin = self.inital_node#start
        route = []
        path = self.path
        prev = ex_dest
        route.append(prev)
        while (prev != origin):
            prev =  path[prev]
            route.append(prev)
        route.reverse()

        #Get list of nodes to go to
        #print(route)
        prev = 0
        road2go = []#]
        for intersection in route:
            if (prev != 0):
                ws = intersections[intersection][prev]
                waynodes = ways[ways.id == ws].nodes.item()
                #print(prev)
                #print(len(waynodes))
                idx_s = waynodes.index(prev)
                idx_f = waynodes.index(intersection)
                if(idx_f>idx_s):
                    for idx in range(idx_s,idx_f):
                        road2go.append(waynodes[idx])
                if(idx_f<idx_s):
                    for idx in range(idx_s,idx_f,-1):
                        road2go.append(waynodes[idx])
                        
            prev = intersection
        print(road2go)
        return road2go


test = gps(97247821)
test.process(thegraph,lengths)
road2go = test.getnodes(340162270)


def test_nav(road2go):
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

test_nav(road2go)










