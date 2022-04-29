#Things

#Configuration
    #range
    #choose roads or buildings

#buildings to OBJ
    
#Roads
import visualization.GUI as gfx
import osmloading.osm as osm

def nodetodot(node):
    pont = osm.getpont(osm.nodetocords(node))
    # print(pont)
    gfx.makeDot(pont)

def add_way_line(way):
    p = 0
    prev = 0
    for x in osm.getWayCartPoints(way):
        p = x
        if (prev != 0):
            x1 = prev[0]
            z1 = prev[1]
            x2 = p[0]
            z2 = p[1]
            gfx.makeLine4(x1,z1,x2,z2)
        prev = p

def draw_line(verts):
    p = 0
    prev = 0
    for x in verts:
        p = x
        if (prev != 0):
            x1 = prev[0]
            z1 = prev[1]
            x2 = p[0]
            z2 = p[1]
            gfx.makeLine4(x1,z1,x2,z2)
        prev = p