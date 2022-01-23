#Get all coords

#Duplicate + add height

#face = pn + p(n+1) + (p(n+1)+h)
#       (pn + h) + (p(n+1)+h) +pn

#Get building number and street


import osmloading.osm as osm
import osmloading.properties as props
import pickle

def make_building_obj(b_id):
    h = osm.scale * 0.01
    b = osm.df_osm[(osm.df_osm.id == b_id )]
    h_data = b[b.tagkey == "building:levels"].tagvalue

    if(len(h_data) != 0):
        h = int((b[b.tagkey == "building:levels"].tagvalue.item()))
        h *= osm.scale * 0.01
        # print(h)

    verts = []
    faces = []
    for x in osm.get_way_locs(b_id):
        p = (osm.localize(osm.latlontocart(x)))
        cord = [p[0],0,p[1]]
        #print(cord)
        verts.append(cord)
    size = len(verts)
    #print(size)
    vc = verts.copy()


    for x in vc:
        cord = [x[0],h,x[2]]
    #    print(cord)
        verts.append(cord)


    #Make Faces
    for x in range (0,size-1):
        points = [x,x+1,x+size]
        p2 = [x+1,x+1+size,x+size]
        faces.append(points)
        faces.append(p2)

    #Make top
    for x in range (0,size-1):
        idx_max = len(verts)-1
        verts[idx_max]
        p = x + size
        points = [p,p+1,idx_max-x]
        faces.append(points)

    fname = osm.base+"objs/buildings/"+ str(b_id) + ".obj"
    objFile = open(fname, 'w')
    print(fname)
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
        objFile.write(str(face[2]+1))
        objFile.write(" ")
        objFile.write(str(face[1]+1))
        objFile.write(" ")
        objFile.write(str(face[0]+1))
        objFile.write("\n")
    objFile.close() 

def obj_and_locs(b_id):
    origin = []
    #Make obj at origin
    h = osm.scale * 0.01
    b = osm.df_osm[(osm.df_osm.id == b_id )]
    h_data = b[b.tagkey == "building:levels"].tagvalue

    if(len(h_data) != 0):
        h = int((b[b.tagkey == "building:levels"].tagvalue.item()))
        h *= osm.scale * 0.01
        # print(h)

    verts = []
    faces = []

    origin.append(osm.localize(osm.latlontocart(osm.get_way_locs(b_id)[0]))[0])
    origin.append(0)
    origin.append(osm.localize(osm.latlontocart(osm.get_way_locs(b_id)[0]))[1])
    # print(origin)

    for x in osm.get_way_locs(b_id):
        p = (osm.localize(osm.latlontocart(x)))
        cord = [p[0]-origin[0],0,p[1]-origin[2]]
        #print(cord)
        verts.append(cord)
    size = len(verts)
    #print(size)
    vc = verts.copy()


    for x in vc:
        cord = [x[0],h,x[2]]
    #    print(cord)
        verts.append(cord)


    #Make Faces
    for x in range (0,size-1):
        points = [x,x+1,x+size]
        p2 = [x+1,x+1+size,x+size]
        faces.append(points)
        faces.append(p2)

    #Make top
    for x in range (0,size-1):
        idx_max = len(verts)-1
        verts[idx_max]
        p = x + size
        points = [p,p+1,idx_max-x]
        faces.append(points)

    objfname = osm.base+"objs/buildings/"+ str(b_id) + ".obj"
    objFile = open(objfname, 'w')
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
        objFile.write(str(face[2]+1))
        objFile.write(" ")
        objFile.write(str(face[1]+1))
        objFile.write(" ")
        objFile.write(str(face[0]+1))
        objFile.write("\n")
    objFile.close() 
    
    #Make loc file to put location
    locfname = osm.base+"locs/buildings/"+ str(b_id) + ".loc"
    with open(locfname, 'wb') as f:
        pickle.dump(origin,f)

#Get points

def make_all_new():
    for building in props.buildings:
        obj_and_locs(building)    

def make_all():
    for building in props.buildings:
        # obj_and_locs(building)
        make_building_obj(building)
#     for wayid in osm.df_ways.id:
#         b = osm.df_osm[(osm.df_osm.id == wayid )]
#         isbuilding = (len(b[b.tagkey=="building"]))
#         if(isbuilding != 0):
#             make_building_obj(wayid)
