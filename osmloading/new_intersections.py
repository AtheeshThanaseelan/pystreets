import osmloading.osm as osm
import osmloading.properties as sts
import math

##TODO: remove nodes that arent it



#Intersections
#Nodeid of intersection
#Wayid of the road that connects the intersections
#Nodeid of the point that the intersection connects to

wayids = sts.roads
ways = osm.df_ways

#NEW data structore for intersections
#Key: Node (intersection)
#Value: Intersection info data structure
    #Key: Node of connected intersection
    #Value: Way that goes to the intersection

intersections = {}

#For all roads
#FIX dest_node METHOD
    #ERRORS caused with 97248035


for wayid in wayids:
    #Nodes of all roads
    nodelist = ways[ways.id == wayid].nodes.item()
    #For each node in the road
    for node in nodelist:
        
        #If the node has been stored previously
        if node in intersections:
            
            #Adding to new structure
            dest_node = 0
            idx = nodelist.index(node)
            max = len(nodelist)
            dest_node = 0
            if(idx == 0):
                dest_node = nodelist[max-1]
            else:
                dest_node = nodelist[0]

            inters_info = intersections[node]
            inters_info.update({dest_node:wayid})
            intersections.update({node:inters_info})

        else:
            #Adding to new structure
            #Hold destination node and way
            inters_info = {}

            dest_node = 0
            idx = nodelist.index(node)
            max = len(nodelist)

            if(idx == 0):
                dest_node = nodelist[max-1]
            else:
                dest_node = nodelist[0]

            inters_info.update({dest_node:wayid})
            intersections.update({node:inters_info})


#Calculate distance of ways
ways = osm.df_ways
nodes = osm.df_nodes
lengths = {}
for intersection in intersections:
    current_conns = intersections[intersection]
    for connected in current_conns:
        way = current_conns[connected]
        if way in lengths:
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
for intersection in intersections:
    curr_inter_weights = {}
    for connected_int in intersections[intersection]:
        way = intersections[intersection][connected_int]
        length = lengths[way]
        curr_inter_weights.update({connected_int:length})
    graph.update({intersection:curr_inter_weights})

def test_all():
    #print(path)
    gfx.setup_gfx()
    drawprop.draw_roads()
    for node in intersections:
        cube = gfx.cube()
        nodetocube(node,1,cube)
        if(node ==97248043):
            gfx.gfx_cubes.append(cube)
    while not gfx.rl.window_should_close():
        gfx.loop()
    gfx.quit_gfx()

def test_connection():
    #Intersection test code (wow)
    gfx.setup_gfx()
    drawprop.draw_roads()
    selected_i = 455753115
    print(intersections[selected_i])
    startnode = gfx.cube()
    startnode.bcolor = gfx.rl.BLUE
    nodetocube(selected_i,0,startnode)
    gfx.gfx_cubes.append(startnode)

    for node in intersection_nodes[selected_i]:
        print(node)
        cube = gfx.cube()
        nodetocube(node,0,cube)
        gfx.gfx_cubes.append(cube)

    for node in intersections[selected_i]:
        cube = gfx.cube()
        nodetocube(node,2,cube)
        gfx.gfx_cubes.append(cube)

    while not gfx.rl.window_should_close():
        gfx.loop()

    gfx.quit_gfx()

    #Debugging the algorithim
    #Draw nodes with cubes
    #Draw way with line(different color?)


def testgraph():
    #print(path)
    gfx.setup_gfx()
    drawprop.draw_roads()
    for node in graph:
        cube = gfx.cube()
        nodetocube(node,1,cube)
        gfx.gfx_cubes.append(cube)
    while not gfx.rl.window_should_close():
        gfx.loop()
    gfx.quit_gfx()
