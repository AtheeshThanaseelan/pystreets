import base.osm as osm
import base.gfx as gfx
import base.properties as sts

wayids = sts.roads
ways = osm.df_ways 

#Stores ways that have a node in common
#Key: Node
#Value: Each way that has the node
intersection_ways = {}
#Stores the intersections that the node connects to
#Key: Node
#Value:
intersection_nodes = {}




#For all roads
for wayid in wayids:
    #Nodes of all roads
    nodelist = ways[ways.id == wayid].nodes.item()
    #For each node in the road
    for node in nodelist:
        #If the node has been stored previously
        if node in intersection_ways:
            #Add the current way to the list of ways with the common node
            waylist = intersection_ways[node]
            waylist.append(wayid)
            intersection_ways.update({node:waylist})

            #Adding to nodelist
            idx = nodelist.index(node)
            if(idx == 0):
                max = len(nodelist)
                nodes = intersection_nodes[node]
                nodes.append(nodelist[max-1])
                intersection_nodes.update({node:nodes})
            else:
                nodes = intersection_nodes[node]
                nodes.append(nodelist[0])
                intersection_nodes.update({node:nodes})

        else:
            #Adding to waylist
            intersection_ways.update({node:[wayid]})

            ##Adding to nodelist
            idx = nodelist.index(node)
            max = len(nodelist)
            if(idx == 0):
                intersection_nodes.update({node:[nodelist[max-1]]})
            else:
                intersection_nodes.update({node:[nodelist[0]]})


#print(len(intersection_nodes))
#print(len(intersection_ways))

i_ways = {}
i_nodes = {}
for intersection in intersection_ways:
    #Get all lines in way, localize, and get dist 
    if(len(intersection_nodes[intersection])>1):
        i_nodes.update({intersection:intersection_nodes[intersection]})
    if(len(intersection_ways[intersection])>1):
        i_ways.update({intersection:intersection_ways[intersection]})

intersection_ways = i_ways
intersection_nodes = i_nodes

# print(len(intersection_nodes))
# print(len(intersection_ways))



# found = inters.found

# osmdf = osm.df_osm
# for ints in found:
#     rnames = []
#     for rs in found[ints]:
#         #print(rs[0])
#         rdf = osmdf[osmdf.id == rs]
#         #print(rs)
#         if (len(rdf[rdf.tagkey == "name"].tagvalue) != 0):
#             rnames.append(rdf[rdf.tagkey == "name"].tagvalue.item())
#     msg = "Found ("+ str(ints) +") intersection connecting: "
#     for n in rnames:
#         msg += n
#         msg += ", "
#     print(msg)






# for x in intersections_ways:
#     print(str(x)+ " has ways" + str(intersections_ways[x]))

# for x in intersections_nodes:
#     print(str(x)+ " connects to intersections " + str(intersections_ways[x]))

