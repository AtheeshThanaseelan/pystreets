#import base.osm as osm
#import base.gfx as gfx
#import base.streets as sts
#import navigation.getIntersections as inters

#Queue

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

#Dijkstra example

ones = {6:14}
ones.update({3:9})
ones.update({2:7})
twos = {1:7}
twos.update({3:10})
twos.update({4:15})
threes = {6:2}
threes.update({4:11})
threes.update({2:10})
threes.update({1:9})
fours = {2:15}
fours.update({3:11})
fours.update({5:6})
fives = {6:9}
fives.update({4:6})
sixs = {1:14}
sixs.update({3:2})
sixs.update({5:9})

graph = {1:ones}
graph.update({2:twos})
graph.update({3:threes})
graph.update({4:fours})
graph.update({5:fives})
graph.update({6:sixs})

##All nodes unvisited. Make unvisited node set
heap = bootlegheap()

##Tentative(shortest total) distance: 0 for initial, inf for all others
heap.add(1,0)
heap.add(2,float('inf'))
heap.add(3,float('inf'))
heap.add(4,float('inf'))
heap.add(5,float('inf'))
heap.add(6,float('inf'))

##Getting paths
path = {}

##Current node: calculate tentative distances through current
quit = 0
curr = (heap.getmin())

while (quit == 0):
    curdists = graph[curr]
    for point in curdists:
        dist = heap.getdist(point)
        newdist = heap.getdist(curr) + curdists[point]
        if(newdist < dist):
            heap.add(point,newdist)
            path.update({point:curr})
    
    ##After all are checked, mark as visited and move on
    graph.pop(curr)
    heap.visited(curr)
    
    ##Next node will be the node with the smallest tentative distance
    curr = (heap.getmin())
    print("next:" + str(curr))
    
    ##If the next node has either already been visted or the distance is inf, STOP
    try:
        graph[curr]
    except:
        print("except")
        quit = 1
    if(heap.getdist(curr) == float('inf')):
        quit = 1

heap.print()
print(path)

#Get the path
ex_dest = 5
origin = 1
route = []
prev = ex_dest
while (prev != origin):
    route.append(prev)
    prev =  path[prev]
route.append(origin)
print(route)

# #Make adjacencies
# roadlinks = {}
# for n in inters.found:
#     for r in inters.found[n]:
#         roadlinks.update({r:inters.found[n]})

