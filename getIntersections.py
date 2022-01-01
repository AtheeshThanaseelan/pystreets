import base.osm as osm
import base.gfx as gfx
import base.streets as sts
import m2D.line_drawroads as roadlines
#print(base.streets.nodes)
#import rep3D.genobj

b = osm.df_osm
#print(b[b.id == 97247821])

#Search ways for common nodes
#TODO: replace with relations
searched = {}
found = {}
w = osm.df_ways
for r in sts.roads:
    ns = (w[w.id==r].nodes.item())
    for n in ns:
        if n in searched:
            if n in found:
                l = found[n]
                l.append(r)
                found.update({n:l})
            else:
                w1 = searched[n]
                ws = [w1,r]
                found.update({n:ws})
        else:
            searched.update({n:r})
osmdf = osm.df_osm
for ints in found:
    rnames = []
    for rs in found[ints]:
        #print(rs[0])
        rdf = osmdf[osmdf.id == rs]
        #print(rs)
        if (len(rdf[rdf.tagkey == "name"].tagvalue) != 0):
            rnames.append(rdf[rdf.tagkey == "name"].tagvalue.item())
    msg = "Found intersection connecting: "
    for n in rnames:
        msg += n
        msg += ", "
    print(msg)

class bike():
    def __init__(self,initialway):
        self.c = gfx.cube()
        self.currroad = sts.roads[345297296]
        self.index = 0
    def loop(self):
        ps = osm.df_nodes[osm.df_nodes.id == self.currroad[self.index]].location.item()
        p = osm.localize(osm.latlontocart(ps))
        self.c.pos = gfx.rl.Vector3(p[0],0,p[1])
        self.index += 1

b = bike(97247821)
roadlines.draw_all()
gfx.setup_gfx()
gfx.gfx_cubes.append(b.c)

count = 0
while True:
    gfx.loop()
    if(count > 100):
        print("k")
        b.loop()
        gfx.gfx_cubes.pop()
        gfx.gfx_cubes.append(b.c)
        count = 0
    count += 1



#r.draw_road(10910476)
#print(sts.roadnames)