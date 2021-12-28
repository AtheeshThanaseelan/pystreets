#Get all coords

#Duplicate + add height

#face = pn + p(n+1) + (p(n+1)+h)
#       (pn + h) + (p(n+1)+h) +pn

import osm

verts = []

for x in osm.getlocs(osm.df_ways,osm.df_nodes,31363751):
    p = (osm.localize(osm.latlontocart(x)))
    cord = [p[0],0,p[1]]
    verts.append(cord)

vc = verts.copy()

for x in vc:
    cord = [x[0],10,x[1]]
    verts.append(cord)

print(verts)
