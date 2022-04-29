# END GOAL:
run a mock traffic simulation using OSM dataset

traffic drives from node to node, making decisions which next road to take at an intersection

## WHAT IS NAVIGATING?:
Travel intersection to intersection down roads

## WHAT IS A INTERSECTION?:
Intersections have lanes going into them and lanes leaving them

## WHAT IS A lane:
a set of points

# STANDARDS:
The Z coordinate, third in the array, is for vertical height
If the start of a lane only connects to one other lane, they are merged into 1 lane
    Lowers amount of intersections
    Can be done later

# IMPLEMENTATION:
## Finding Intersections
WE HAVE: A bunch of roads, some oneway, some multilane

FIRST: make lanes for each road, store them somewhere

    This solves issue of oneway lanes

    the order of points in the object is the traversal direction

    lane object has left lane, right lane, main lane(for oneway roads)

    When making each lane:

        Store the starting and ending nodes(intersections here)
            Start and end seperately


SECOND: Get intersections

    Loop through all the end nodes

        If it exists in start nodes, store it as {startNode, corresponding lane}

THIRD: Export Lanes and Intersections




# TODO:
intersections
    proper way of checking for intersections, not guessing by first/last node in ways
    check one way nodes
    deadend roads


Tests
    Test Intersections
    Test Lanes
    Test Navigation (all possible routes)
        Random start points

GPS
    Save completed routes to prevent a redo
    Save heap
    Save route
    Access with GPS

EXPORT
    JSON




# DONE:
osm.py needs organization
    Functions for points > cartesian
lanes
    one way roads
GUI
    TKINTER