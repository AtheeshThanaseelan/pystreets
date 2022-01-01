import base.osm as osm
import os
#import ps

#Got road name
#Got road nodes

#Traverse: loop through

roadnames = {}
roads = {}

#Node to Cordinate

#Way to Cordinate


def getroads():
    b = osm.df_osm
    h = b[b.tagkey=="highway"]
    valcond = (b.tagvalue == "tertiary") | (b.tagvalue == "secondary") | (b.tagvalue == "residential")
    r = h[valcond]
    #print(r.id)

    #Get road properties
    for x in r.id:
        #print(x)
        p = b[b.id == x]
        ws = osm.df_ways
        n = ws[ws.id == x]
        name = p[p.tagkey =="name"]
        if(len(name) != 1):
            roads.update({x:n.nodes.item()})
        elif(len(name) == 1):
            roads.update({x:n.nodes.item()})    
            if(name.tagvalue.item() in roadnames):
                #print("dup")
                temp = roadnames.get(name.tagvalue.item()).copy()
                for newnodes in n.nodes.item():
                    #print(newnodes)
                    temp.append(newnodes)
                roadnames.update({name.tagvalue.item():temp})
            else:
                roadnames.update({name.tagvalue.item():n.nodes.item()})
                

getroads()



#nodes = (roadnames["Grenoble Drive"])
#print(roads.keys())
#nodes = roads.get(345297296)
# rpoints = []
# for x in nodes:
#     a = osm.nodetocords(x)
#     b = osm.latlontocart(a)
#     c = osm.localize(b)
#     rpoints.append(c)

if __name__ == "__main__":
    for x in roads:
        ps.add_way_line(x)
    ps.gfx.setup_gfx()
    roadpos = 0
    print(len(rpoints))
    count = 0
    p=0

    c = ps.gfx.cube()
    ps.gfx.gfx_cubes.append(c)

    while(True):
        print(roadpos)
        c.pos = ps.gfx.rl.Vector3(rpoints[roadpos][0],0,rpoints[roadpos][1])
        if(count > 100):
            if(roadpos == len(rpoints)-1):
                roadpos = -1
            roadpos = roadpos + 1
            count = 0
        count = count + 1
        ps.gfx.loop()

#gfx.quit_gfx()
