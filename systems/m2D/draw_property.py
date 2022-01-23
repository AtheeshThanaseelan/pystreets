import systems.m2D.tools as tools
import osmloading.properties
import osmloading.osm as osm
import base.gfx as gfx
import math

def draw_roads():
    for r_id in osmloading.properties.roads:
        tools.add_way_line(r_id)

def draw_buildings():
    for b_id in osmloading.properties.buildings:
        tools.add_way_line(b_id)