#Get all coords

#Duplicate + add height

#face = pn + p(n+1) + (p(n+1)+h)
#       (pn + h) + (p(n+1)+h) +pn

#Get building number and street


import osm

def make_building_obj(b_id):
    h = 1
    b = osm.df_osm[(osm.df_osm.id == b_id )]
    h_data = b[b.tagkey == "building:levels"].tagvalue

    if(len(h_data) != 0):
        h = int((b[b.tagkey == "building:levels"].tagvalue.item()))
        print(h)

    verts = []
    faces = []
    for x in osm.getlocs(osm.df_ways,osm.df_nodes,b_id):
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


    fname = "./objs/"+ str(b_id) + ".obj"
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
#Get points


for wayid in osm.df_ways.id:
    b = osm.df_osm[(osm.df_osm.id == wayid )]
    isbuilding = (len(b[b.tagkey=="building"]))
    if(isbuilding != 0):
        make_building_obj(wayid)
    

import testobj

#print(size)
#print(verts[13])