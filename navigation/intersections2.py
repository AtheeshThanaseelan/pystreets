import osmloading.osm as osm
import osmloading.properties as sts
import navigation.lanes2 as lanes2
import math

#Intersection: Collection of start nodes and end nodes
    #Get a intersection from a end node going into the intersection
    #Get a start node as a lane

#Calculating: 
    #Duplicate end and start nodes overall
        #Store end nodes dict; node : road_id
        #Store start nodes dict; node : road_id
    #Loop through end nodes
        #See if there are start nodes matching the end node
        #Store intersection as nodeid : intersection obj
    
#Testing:
    #Start at node
    #Display list of next possible lanes
    #Progress through lane to next intersection
    #Visualize with GUI + Circle to represent current location
        #Button/Terminal to advance?

wayids = sts.roads
ways = osm.df_ways

lanes = lanes2.lanes

end_nodes = [] #FIX: LIST TO DICT
startNodeAndRoad = {}
intersections = {}
class intersection:
    def __init__(self) -> None:
        self.inroads = []
        self.outroads = []
        pass

for lane_id in lanes:
    if(lanes[lane_id].mainLane == 0):
        end_nodes.append(lanes[lane_id].endNode)
        startNodeAndRoad.update({lanes[lane_id].startNode:lane_id})
    elif(lanes[lane_id].mainLane == 0):
        end_nodes.append(lanes[lane_id].endNode)
        startNodeAndRoad.update({lanes[lane_id].startNode:lane_id})
        end_nodes.append(lanes[lane_id].startNode)
        startNodeAndRoad.update({lanes[lane_id].endNode:lane_id})


for end_node in end_nodes:
    if end_node in startNodeAndRoad:
        if end_node in intersections:
            current_inter = intersections[end_node]
            #Store wayID of incoming road
            #Store wayID of outgoing road
        else:
            current_inter = intersection()
            #Store wayID of incoming road
            #Store wayID of outgoing road

    print(end_node)