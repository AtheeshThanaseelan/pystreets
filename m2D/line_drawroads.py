import base.streets
import base.osm as osm
import base.gfx as gfx
import math

def draw_all():
    for x in base.streets.roads:
        draw_road(x)

def draw_road(b_id):
    verts = []
    faces = []
    for x in osm.getlocs(osm.df_ways,osm.df_nodes,b_id):
        p = (osm.localize(osm.latlontocart(x)))
        cord = [p[0],0,p[1]]
        print(cord)
        verts.append(cord)

    prev_p = 0
    for i in range(0,math.floor(len(verts))):
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


    