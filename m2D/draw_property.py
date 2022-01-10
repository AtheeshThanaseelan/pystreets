import m2D.tools as tools
import base.properties
import base.osm as osm
import base.gfx as gfx
import math

def draw_roads():
    for r_id in base.properties.roads:
        tools.add_way_line(r_id)

def draw_buildings():
    for b_id in base.properties.buildings:
        tools.add_way_line(b_id)