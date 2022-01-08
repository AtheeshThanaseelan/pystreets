import navigation.getIntersections as inters
import base.streets as sts
import base.osm as osm
import navigation.traverse as trav
import math

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

#(node:[waylist])
intersections_ways  = inters.intersection_ways
#(node:[nodelist])
intersections_nodes  = inters.intersection_nodes
#Name nodes
roadnames = sts.roadnames

#Calculate distance of ways
ways = osm.df_ways
nodes = osm.df_nodes
lengths = {}
for intersection in intersections_ways:
    for way in intersections_ways[intersection]:
        if ((way in lengths)):
            None
        else:
            waynodes = ways[ways.id == way].nodes.item()
            tdist = 0
            prev = 0
            for node in waynodes:
                if prev == 0:
                    prev = node
                else:
                    loc = osm.getpont(nodes[nodes.id == node].location.item())
                    prevloc = osm.getpont(osm.nodetocords(prev))
                    dist = math.sqrt((loc[0]-prevloc[0])**2 * (loc[1]-prevloc[1])**2)
                    tdist = dist + tdist
                    #print(dist)
            lengths.update({way:tdist})


#Process connections with djistra graph
#Make graph structure
graph = {}
for inter in intersections_ways:
    #print(inter)
    curr_inter_weights = {}
    idx = 0
    for way in intersections_ways[inter]:
        curr_inter_weights.update({intersections_nodes[inter][idx]:lengths[way]})
        idx += 1
    graph.update({inter:curr_inter_weights})

##Holding paths (node to node)
path = {}

##Run djistakara 
heap = bootlegheap()
start = 97247821
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


#Get the path
ex_dest = 97247887
origin = start
route = []
prev = ex_dest
route.append(prev)
while (prev != origin):
    prev =  path[prev]
    route.append(prev)
route.reverse()
#print(route)
print(route)
prev = 0
for x in route:
    if (prev != 0):
        ws = intersections_ways[x]
        prev_ws = intersections_ways[x]
        same = []
        for w in ws:
            for prevw in prev_ws:
                if w == prevw:
                    same.append(w)
        print(same)
        #get list of ways at node
        #compare to other list of ways
    prev = x



#for x in route:
#    trav.go(x)
