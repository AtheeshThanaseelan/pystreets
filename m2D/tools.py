#Things

#Configuration
    #range
    #choose roads or buildings

#buildings to OBJ
    
#Roads
import base.gfx as gfx
import base.osm as osm

def nodetocube(node,h,cube):
    pont = osm.getpont(osm.nodetocords(node))
    print(pont)
    cube.setpos(pont[0],h,pont[1])

def add_way_line(way):
    p = 0
    prev = 0
    for x in osm.get_way_locs(way):
        p = osm.getpont(x)
        if (prev == 0):
            1
        else:
            l = gfx.line()
            l.x1 = prev[0]
            l.z1 = prev[1]
            l.x2 = p[0]
            l.z2 = p[1]
            gfx.gfx_lines.append(l)
        prev = p
