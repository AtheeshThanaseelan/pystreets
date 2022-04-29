#Lanes
#Key: Road Way ID
#Value: Left Lane, Right Lane


#Finding the lane:
#When calculating, know first node and last node
#First node: takes left
#Last node: takes right


#Storing Lanes
#If we want to know what lane to go down
    #Check start of left and start of right, then use that?
    #Store left and right by start node
        #{start node, waylist}

#Using Lanes
#Choose road, get lanes from road, get origin lane

import osmloading.osm as osm
import osmloading.properties as sts
import math

def make_streetlanes(way):
    roadlent = 0.5 * osm.scale * 0.01
    leftlane = []
    rightlane = []
    verts = []
    for x in osm.getWayCartPoints(way):
        p = (osm.localize(osm.latlontocart(x)))
        cord = [p[0],0,p[1]]
        verts.append(cord)
    size = len(verts)


    #Add verticies to make 2D road
    prev_p = 0
    for x in verts:
        if(prev_p != 0):

            #Get direction vector
            dvec = [0,0,0]
            dvec[0] = (x[0]-prev_p[0])
            dvec[2] = (x[2]-prev_p[2])
            #x formula: prev[0] + dvec[0]*t
            #y formula: prev[1] + dvec[1]*t
            
            #Get perpendicular direction vector
            perp_dvec = []
            perp_dvec.append(-dvec[2])
            perp_dvec.append(0)
            perp_dvec.append(dvec[0])

            #Find "t" using line length
            length = math.sqrt((math.pow((dvec[0]),2) + math.pow((dvec[2]),2)))
            t = (roadlent / length) * 1
            t2 = 0

            ##Make point parallel to prev
            #Get a perpendicular point
            prev_perp_point = []
            prev_perp_point.append((prev_p[0] + perp_dvec[0]*t))
            prev_perp_point.append(0)
            prev_perp_point.append((prev_p[2] + perp_dvec[2]*t))
            
            #Get a point parallel to prev
            parallel_point_prev = []
            parallel_point_prev.append((prev_perp_point[0] + dvec[0]*t2))
            parallel_point_prev.append(0)
            parallel_point_prev.append((prev_perp_point[2] + dvec[2]*t2))

            ##Make point parallel to current
            #Get perpendicular point
            current_perp_point = []
            current_perp_point.append((x[0] + perp_dvec[0]*t))
            current_perp_point.append(0)
            current_perp_point.append((x[2] + perp_dvec[2]*t))
            
            #Get a point parallel to current
            parallel_point = []
            parallel_point.append((current_perp_point[0] + dvec[0]*t2))
            parallel_point.append(0)
            parallel_point.append((current_perp_point[2] + dvec[2]*t2))

        
            leftlane.append(parallel_point_prev)
            leftlane.append(parallel_point)


        prev_p = x
    
    #Do the same for the other side
    prev_p = 0
    for x in verts:
        if(prev_p != 0):

            #Get direction vector
            dvec = [0,0,0]
            dvec[0] = (x[0]-prev_p[0])
            dvec[2] = (x[2]-prev_p[2])
            #x formula: prev[0] + dvec[0]*t
            #y formula: prev[1] + dvec[1]*t
            
            #Get perpendicular direction vector
            perp_dvec = []
            perp_dvec.append(-dvec[2])
            perp_dvec.append(0)
            perp_dvec.append(dvec[0])

            #Find "t" using line length
            length = math.sqrt((math.pow((dvec[0]),2) + math.pow((dvec[2]),2)))
            t = (roadlent / length) * -1
            t2 = 0

            ##Make point parallel to prev
            #Get a perpendicular point
            prev_perp_point = []
            prev_perp_point.append((prev_p[0] + perp_dvec[0]*t))
            prev_perp_point.append(0)
            prev_perp_point.append((prev_p[2] + perp_dvec[2]*t))
            
            #Get a point parallel to prev
            parallel_point_prev = []
            parallel_point_prev.append((prev_perp_point[0] + dvec[0]*t2))
            parallel_point_prev.append(0)
            parallel_point_prev.append((prev_perp_point[2] + dvec[2]*t2))

            ##Make point parallel to current
            #Get perpendicular point
            current_perp_point = []
            current_perp_point.append((x[0] + perp_dvec[0]*t))
            current_perp_point.append(0)
            current_perp_point.append((x[2] + perp_dvec[2]*t))
            
            #Get a point parallel to current
            parallel_point = []
            parallel_point.append((current_perp_point[0] + dvec[0]*t2))
            parallel_point.append(0)
            parallel_point.append((current_perp_point[2] + dvec[2]*t2))

        
            rightlane.append(parallel_point_prev)
            rightlane.append(parallel_point)


        prev_p = x


    return leftlane, rightlane


lanes = {}
wayids = sts.roads

for r_id in wayids:
    object = osm.df_osm[osm.df_osm.id == r_id]
    oneway = False
    try:
        if(object[object.tagkey == "oneway"].tagvalue.item() == "yes"):
            oneway = True
    except:
        oneway = False
    if oneway == False:
        left, right = make_streetlanes(r_id)
        value = [left,right]
        lanes.update({r_id:value})
    # else:
        # lanes.update({r_id:sts.roads[r_id]})
