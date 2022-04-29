import osmloading.osm as osm
import osmloading.properties as sts
import math


#SECOND: Get intersections

#    Loop through all the end nodes

#        If it exists in start nodes, store it as {startNode, corresponding lane}

#At the end of the lane, what new lanes are available
    #Loop through end nodes, find it in start nodes


wayids = sts.roads
ways = osm.df_ways


intersections = {}

#Get intersections
#For all nodes, see if there is a road with the matching node
for wayid in wayids:
    #Nodes of all roads
    nodelist = ways[ways.id == wayid].nodes.item()
    #For each node in the road
    for node in nodelist:
        # if node == 97248035:
        #     None
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
                    loc = osm.getNodeCartesian(node)
                    prevloc = osm.getNodeCartesian(prev)
                    dist = math.sqrt((loc[0]-prevloc[0])**2 * (loc[1]-prevloc[1])**2)
                    tdist = dist + tdist
                    #print(dist)
            lengths.update({way:tdist})



