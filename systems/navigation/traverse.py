# import systems.navigation.getIntersections as intersections
# import m2D.draw_property as draw_prop
# import osmloading.osm as osm
# import base.gfx as gfx

# class bike():
#     def __init__(self,initialway):
#         self.c = gfx.cube()
#         self.currroad = intersections.sts.roads[initialway]
#         self.lenth = len(self.currroad)-1
#         print(self.lenth)
#         self.index = 0
#     def loop(self):
#         ps = osm.df_nodes[osm.df_nodes.id == self.currroad[self.index]].location.item()
#         p = osm.localize(osm.latlontocart(ps))
#         self.c.pos = gfx.rl.Vector3(p[0],0,p[1])
#         self.index += 1

# def go(way):
#     b = bike(way)
#     b.loop()
#     draw_prop.draw_roads()
#     gfx.setup_gfx()
#     gfx.gfx_cubes.append(b.c)

#     count = 0
#     while True:
#         try:
#             gfx.loop()
#             if(count > 10):
#                 print("k")
#                 b.loop()
#                 gfx.gfx_cubes.pop()
#                 gfx.gfx_cubes.append(b.c)
#                 count = 0
#             count += 1
#             if(b.index > b.lenth):
#                 break
#         except KeyboardInterrupt:
#             break
#     gfx.quit_gfx()