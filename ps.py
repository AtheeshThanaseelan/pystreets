#Things

#Configuration
    #range
    #choose roads or buildings

#buildings to OBJ
    
#Roads
import gfx
import osm

def add_way_line(way):
    p = 0
    prev = 0
    for x in osm.getlocs(osm.df_ways,osm.df_nodes,way):
        p = (osm.localize(osm.latlontocart(x)))
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
def run_gfx():
    gfx.setup_gfx()
    while(True):
        gfx.loop()

    gfx.quit_gfx()

def traverse_street(street):
    #For straight street (2 points)
    slope = (street[0][1]-street[1][1])/(street[0][0]-street[1][0])
    y_icept = street[0][1] - slope*street[0][0]
    pos = slope*timestamp + y_icept
    return pos

def run():
    for x in range(0,10):
        print(traverse_street(streets[0]))
        timestamp = timestamp + 1

if __name__ == "__main__":

    objects = []

    gfx.setup_gfx()


    linecount = 0
    for way in osm.df_osm[osm.df_osm.tagkey == "highway"].id:
        for way in osm.df_ways.id:
            p = 0
            prev = 0
            linecount = linecount + 1
            if(linecount > 100):
                0
            else:
                for x in osm.getlocs(osm.df_ways,osm.df_nodes,way):
                    p = (osm.localize(osm.latlontocart(x)))
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
    # p = 0
    # prev = 0
    # for x in osm.getlocs(osm.df_ways,osm.df_nodes,31363751):
    #     p = (osm.localize(osm.latlontocart(x)))
    #     if (prev == 0):
    #         1
    #     else:
    #         l = gfx.line()
    #         l.x1 = prev[0]
    #         l.z1 = prev[1]
    #         l.x2 = p[0]
    #         l.z2 = p[1]
    #         gfx.gfx_lines.append(l)
    #     prev = p





    while(True):
        gfx.loop()

    gfx.quit_gfx()


    streets = [[[0,0],[1,10]]]
    #print(streets[0])
    timestamp = 0

    #Graph navigation

    #Store streets somehow
        #Streets are a set of point (directional)

    #Traverse point to point
