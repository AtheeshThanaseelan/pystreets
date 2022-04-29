import osmloading.osm as osm
import osmloading.properties as sts
import math


class lane:
    def __init__(self):
        self.mainLane = 0
        self.leftLane = []
        self.rightLane = []


def make_streetlanes(way):
    roadlent = 0.5 * osm.scale * 0.01
    leftlane = []
    rightlane = []
    verts = []
    for x in osm.getWayCartPoints(way):
        verts.append(x)

    size = len(verts)


    #Add verticies to make 2D road
    prev_p = 0
    for x in verts:
        if(prev_p != 0):

            #Get direction vector
            dvec = [0,0,0]
            dvec[0] = (x[0]-prev_p[0])
            dvec[1] = (x[1]-prev_p[1])
            #x formula: prev[0] + dvec[0]*t
            #y formula: prev[1] + dvec[1]*t
            
            #Get perpendicular direction vector
            perp_dvec = []
            perp_dvec.append(-dvec[1])
            #perp_dvec.append(0)
            perp_dvec.append(dvec[0])

            #Find "t" using line length
            length = math.sqrt((math.pow((dvec[0]),2) + math.pow((dvec[1]),2)))
            t = (roadlent / length) * 1
            t2 = 0

            ##Make point parallel to prev
            #Get a perpendicular point
            prev_perp_point = []
            prev_perp_point.append((prev_p[0] + perp_dvec[0]*t))
            #prev_perp_point.append(0)
            prev_perp_point.append((prev_p[1] + perp_dvec[1]*t))
            
            #Get a point parallel to prev
            parallel_point_prev = []
            parallel_point_prev.append((prev_perp_point[0] + dvec[0]*t2))
            #parallel_point_prev.append(0)
            parallel_point_prev.append((prev_perp_point[1] + dvec[1]*t2))

            ##Make point parallel to current
            #Get perpendicular point
            current_perp_point = []
            current_perp_point.append((x[0] + perp_dvec[0]*t))
            #current_perp_point.append(0)
            current_perp_point.append((x[1] + perp_dvec[1]*t))
            
            #Get a point parallel to current
            parallel_point = []
            parallel_point.append((current_perp_point[0] + dvec[0]*t2))
            #parallel_point.append(0)
            parallel_point.append((current_perp_point[1] + dvec[1]*t2))

        
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
            dvec[1] = (x[1]-prev_p[1])
            #x formula: prev[0] + dvec[0]*t
            #y formula: prev[1] + dvec[1]*t
            
            #Get perpendicular direction vector
            perp_dvec = []
            perp_dvec.append(-dvec[1])
            #perp_dvec.append(0)
            perp_dvec.append(dvec[0])

            #Find "t" using line length
            length = math.sqrt((math.pow((dvec[0]),2) + math.pow((dvec[1]),2)))
            t = (roadlent / length) * -1
            t2 = 0

            ##Make point parallel to prev
            #Get a perpendicular point
            prev_perp_point = []
            prev_perp_point.append((prev_p[0] + perp_dvec[0]*t))
            #prev_perp_point.append(0)
            prev_perp_point.append((prev_p[1] + perp_dvec[1]*t))
            
            #Get a point parallel to prev
            parallel_point_prev = []
            parallel_point_prev.append((prev_perp_point[0] + dvec[0]*t2))
            #parallel_point_prev.append(0)
            parallel_point_prev.append((prev_perp_point[1] + dvec[1]*t2))

            ##Make point parallel to current
            #Get perpendicular point
            current_perp_point = []
            current_perp_point.append((x[0] + perp_dvec[0]*t))
            #current_perp_point.append(0)
            current_perp_point.append((x[1] + perp_dvec[1]*t))
            
            #Get a point parallel to current
            parallel_point = []
            parallel_point.append((current_perp_point[0] + dvec[0]*t2))
            #parallel_point.append(0)
            parallel_point.append((current_perp_point[1] + dvec[1]*t2))

        
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

    currentLane = lane()
    if oneway == False:
        #Flip the left/right lane order???
        currentLane.leftLane, currentLane.rightLane = make_streetlanes(r_id)
        lanes.update({r_id:currentLane})
    else:
        #Ensure one way roads go in the right direction???
        print(r_id)
        currentLane.mainLane = osm.getWayCartPoints(r_id)
        lanes.update({r_id:currentLane})


#TODO
#Store lane lengths
#Store lane start nodes
#Store lane end nodes