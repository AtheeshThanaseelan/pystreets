import osmloading.osm as osm
import osmloading.properties as sts
import navigation.lanes2 as lanes2
import math


#SECOND: Get intersections

#   Loop through all the end nodes
#       If it exists as start nodes, store it as {startNode, corresponding lane}

#   At the end of the lane, what new lanes are available
#       Loop through end nodes, find it in start nodes

#Intersection: Collection of start nodes and end nodes
    #Get a intersection from a end node going into the intersection
    #Get a start node as a lane

#Calculating: 
    #Duplicate end and start nodes overall
        #Store end nodes as a list
        #Store start nodes dict; node : road_id
    #Loop through end nodes
        #See if there are start nodes
        #
    
#Testing:
    #Start at node
    #Display list of next possible lanes
    #Progress through lane to next intersection
    #Visualize with GUI + Circle to represent current location
        #Button/Terminal to advance?

wayids = sts.roads
ways = osm.df_ways

lanes = lanes2.lanes

end_node = []
startNodeAndRoad = {}

for lane_id in lanes:
    if(lanes[lane_id].mainLane == 0):
        end_node.append(lanes[lane_id].endNode)
        startNodeAndRoad.update({lanes[lane_id].startNode:lane_id})
    elif(lanes[lane_id].mainLane == 0):
        end_node.append(lanes[lane_id].endNode)
        startNodeAndRoad.update({lanes[lane_id].startNode:lane_id})
        end_node.append(lanes[lane_id].startNode)
        startNodeAndRoad.update({lanes[lane_id].endNode:lane_id})