import osmloading.properties as streets
import osmloading.osm as osm
import base.gfx as gfx
import math

vlist = []
way_df = osm.df_ways

#fae = []

def make_street_obj(b_id):
    roadlent = 0.1
    rl_signed = 0
    verts = []
    faces = []
    for x in osm.get_way_locs(b_id):
        p = (osm.localize(osm.latlontocart(x)))
        cord = [p[0],0,p[1]]
        #print(cord)
        verts.append(cord)
    size = len(verts)
    #print(verts)
    vc = verts.copy()

    #Add verticies to make 2D road
    prev_p = 0
    m = 0
    for x in vc:
        cord = 0
        if(prev_p == 0):
            0
        else:
            m = (x[2] -prev_p[2])/(x[0]-prev_p[0])
            m = -1/m
            b = prev_p[2] - m*prev_p[0]
            if( m > 0  ):
                rl_signed = roadlent * -1
            else:
                rl_signed = roadlent * 1
            cord = [0,0,prev_p[2]+rl_signed]
            cord[0] = (cord[2]-b)/m
            verts.append(cord)

        prev_p = x
    cord = [0,0,prev_p[2]+0.1]
    b = prev_p[2] - m*prev_p[0]
    cord[0] = (cord[2]-b)/m
    verts.append(cord)

    for x in range(0,size-1):
        points = [x,x+1,size+x]
        faces.append(points)
        #p2 = [x+1,x+1+size,x+size]
        #faces.append(p2)
    vlist.append(verts)
    fname = "working/objs/streets/"+ str(b_id) + ".obj"
    objFile = open(fname, 'w')
    for vert in verts:
        objFile.write("v ")
        objFile.write(str(vert[0]))
        objFile.write(" ")
        objFile.write(str(vert[1]))
        objFile.write(" ")
        objFile.write(str(vert[2]))
        objFile.write("\n")
    for face in faces:
        objFile.write("f ")
        objFile.write(str(face[0]+1))
        objFile.write(" ")
        objFile.write(str(face[1]+1))
        objFile.write(" ")
        objFile.write(str(face[2]+1))
        objFile.write("\n")
    objFile.close() 

def make_streetobj_2(way):
    #way = 345297296#374037049
    #way = 374037049
    roadlent = 0.5 * osm.scale * 0.01

    verts = []
    obj_verts = []
    obj_faces = []
    for x in osm.get_way_locs(way):
        p = (osm.localize(osm.latlontocart(x)))
        cord = [p[0],0,p[1]]
        verts.append(cord)
    size = len(verts)
    #print(size)
    #vc = verts.copy()

    #Add verticies to make 2D road
    prev_p = 0
    idx = 0
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
            #print(length)

            ##Make point parallel to prev
            #Get a perpendicular point
            perp_point = []
            perp_point.append((prev_p[0] + perp_dvec[0]*t))
            perp_point.append(0)
            perp_point.append((prev_p[2] + perp_dvec[2]*t))
            
            #Get a point parallel to prev
            parallel_point_prev = []
            parallel_point_prev.append((perp_point[0] + dvec[0]*t2))
            parallel_point_prev.append(0)
            parallel_point_prev.append((perp_point[2] + dvec[2]*t2))
            #verts.append(parallel_point_prev)

            ##Make point parallel to current
            #Get perpendicular point
            perp_point = []
            perp_point.append((x[0] + perp_dvec[0]*t))
            perp_point.append(0)
            perp_point.append((x[2] + perp_dvec[2]*t))
            
            #Get a point parallel to current
            parallel_point = []
            parallel_point.append((perp_point[0] + dvec[0]*t2))
            parallel_point.append(0)
            parallel_point.append((perp_point[2] + dvec[2]*t2))
            #verts.append(parallel_point)

            obj_verts.append(prev_p)
            obj_verts.append(x)
            obj_verts.append(parallel_point_prev)
            obj_faces.append([idx+2,idx+1,idx])

            obj_verts.append(parallel_point)
            obj_faces.append([idx+1,idx+2,idx+3])

            idx += 4
            

        prev_p = x


    fname = "working/objs/streets/"+ str(way) + ".obj"
    objFile = open(fname, 'w')
    for vert in obj_verts:
        objFile.write("v ")
        objFile.write(str(vert[0]))
        objFile.write(" ")
        objFile.write(str(vert[1]))
        objFile.write(" ")
        objFile.write(str(vert[2]))
        objFile.write("\n")
    for face in obj_faces:
        objFile.write("f ")
        objFile.write(str(face[0]+1))
        objFile.write(" ")
        objFile.write(str(face[1]+1))
        objFile.write(" ")
        objFile.write(str(face[2]+1))
        objFile.write("\n")
    objFile.close() 

for x in streets.roads:
    #print(x)
    #make_street_obj(x)
    make_streetobj_2(x)
    print(x)

#make_street_obj(244475672)
#make_street_obj(31653250)
#make_street_obj(345297296)
# print(len(vlist))

# count = 0
# for verts in vlist:
#     prev_p = 0
#     #print(len(verts))
#     for p in verts:
#         count = count + 1
#         if(count < 300):
#             c = gfx.cube()
#             c.xsize = 0.1
#             c.ysize = 0.1
#             c.zsize = 0.1
#             c.pos = gfx.rl.Vector3(p[0], 0.0, p[2])
#             gfx.gfx_cubes.append(c)
        
#     for i in range(0,math.ceil(len(verts)/2)):
#         #print(i)
#         cord = 0
#         if(prev_p == 0):
#             0
#         else:
#             l = gfx.line()
#             l.x1 = prev_p[0] 
#             l.z1 = prev_p[2]
#             l.x2 = verts[i][0]
#             l.z2 = verts[i][2]
#             gfx.gfx_lines.append(l)

#         prev_p = verts[i]
#     prev_p = 0
#     for i in range(len(verts)-1,math.floor(len(verts)/2)-1,-1):
#         #print(i)
#         cord = 0
#         if(prev_p == 0):
#             0
#         else:
#             l = gfx.line()
#             l.x1 = prev_p[0] 
#             l.z1 = prev_p[2]
#             l.x2 = verts[i][0]
#             l.z2 = verts[i][2]
#             gfx.gfx_lines.append(l)

#         prev_p = verts[i]

# gfx.setup_gfx()
# while True:
#     gfx.loop()