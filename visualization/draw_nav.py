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
            #draw left lane
            tools.draw_line(lanes.lanes[lane].leftLane)
            #draw start of left lane
            start = lanes.lanes[lane].leftLane[0]
            start.append(10)
            tools.gfx.makeDotColor(start,"red")
            #draw right lane
            tools.draw_line(lanes.lanes[lane].rightLane)
            #draw start of right lane
            rstart = lanes.lanes[lane].rightLane[0]
            rstart.append(5)
            tools.gfx.makeDotColor(rstart,"blue")
