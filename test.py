import streets
import osm
import gfx
import math

verts = []
faces = []

def make_street_obj(b_id):
    verts = []
    faces = []
    for x in osm.getlocs(osm.df_ways,osm.df_nodes,b_id):
        p = (osm.localize(osm.latlontocart(x)))
        cord = [p[0],0,p[1]]
        #print(cord)
        verts.append(cord)
    size = len(verts)
    print(verts)
    vc = verts.copy()

    #Add verticies to make 2D road
    prev_p = 0
    for x in vc:
        cord = 0
        if(prev_p == 0):
            0
        else:
            cord = [0,0,x[2]+0.01]
            m = (x[2] -prev_p[2])/(x[0]-prev_p[0])
            m = -1/m
            b = x[2] - m*x[0]
            cord[0] = (cord[2]-b)/m
            #cord[0] = m*cord[2] + b
            verts.append(cord)

        prev_p = x
        
    for x in range(0,size-1):
        points = [x,x+1,size+x]
        faces.append(points)
        p2 = [x+1,x+1+size,x+size]
        faces.append(p2)

    fname = "./objs/streets/"+ str(b_id) + ".obj"
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

for x in streets.roads:
    print(x)
    make_street_obj(x)

prev_p = 0
count = 0
for i in range(0,math.floor(len(verts)/2)):
    cord = 0
    if(prev_p == 0):
        0
    else:
        l = gfx.line()
        l.x1 = prev_p[0] 
        l.z1 = prev_p[2]
        l.x2 = verts[i][0]
        l.z2 = verts[i][2]
        gfx.gfx_lines.append(l)

    prev_p = verts[i]
#prev_p = 0
for i in range(len(verts)-1,math.floor(len(verts)/2),-1):
    cord = 0
    if(prev_p == 0):
        0
    else:
        l = gfx.line()
        l.x1 = prev_p[0] 
        l.z1 = prev_p[2]
        l.x2 = verts[i][0]
        l.z2 = verts[i][2]
        gfx.gfx_lines.append(l)

    prev_p = verts[i]

gfx.setup_gfx()
while True:
    gfx.loop()