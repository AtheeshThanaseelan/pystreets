import visualization.tools as tools
import navigation.lanes2 as lanes
import navigation.new_intersections as inters
# import osmloading.lanes_approx as lanes
import osmloading.osm as osm
import math


def draw_lanes():
    print("ok")
    for lane in lanes.lanes:
        if(lanes.lanes[lane].mainLane != 0 ):
            tools.draw_line(lanes.lanes[lane].mainLane)
            start = lanes.lanes[lane].mainLane[0]
            start[2] = 10
            # tools.gfx.makeDotColor(start,"red")
            end = lanes.lanes[lane].mainLane[-1]
            end[2] = 5
            # tools.gfx.makeDotColor(end,"blue")
        else:
            tools.draw_line(lanes.lanes[lane].leftLane)
            start = lanes.lanes[lane].leftLane[0]
            start.append(10)
            tools.gfx.makeDotColor(start,"red")
            tools.draw_line(lanes.lanes[lane].rightLane)
            rstart = lanes.lanes[lane].rightLane[0]
            rstart.append(10)
            tools.gfx.makeDotColor(rstart,"blue")
