#Intersections
#Nodeid of intersection
#Wayid of the road that connects the intersections
#Nodeid of the point that the intersection connects to

wayids = sts.roads
ways = osm.df_ways

#Key: Node
#Value: Each way that has the node
intersection_ways = {}

#Key: Node
#Value:
intersection_nodes = {}


for wayid in wayids:
    nodelist = ways[ways.id == wayid].nodes.item()
    for node in nodelist:
        if node in intersection_ways:
            #Adding to waylist
            waylist = intersection_ways[node]
            waylist.append(wayid)
            intersection_ways.update({node:waylist})

            #if(wayid == 551682469):
            #    print(nodelist[max-1])

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

print(intersection_nodes)

#GPS Class
#Objects:
#   Initial
#   Graph
#   
#Init:
#   Starting intersection
#Process:
#   Run djistra
#Get Path:
#   Take destination
#   Return ????



#Traverse
#Way
#Which side of the way to enter from
