import osmloading.osm as osm

#Get road name
#Get road nodes
roadnames = {}
roads = {}

#Get building ways
buildings = {}
buildingnames = {}

#Intersections


def getroads():
    allroads_df = osm_df[osm_df.tagkey=="highway"]
    roadtags = (osm_df.tagvalue == "tertiary") | (osm_df.tagvalue == "secondary") | (osm_df.tagvalue == "residential")
    roads_df = allroads_df[roadtags]

    for x in roads_df.id:
        nodelist = ws[ws.id == x].nodes.item()
        roads.update({x:nodelist})

        object = osm_df[osm_df.id == x]
        name_df = object[object.tagkey =="name"]
        # print(object[object.tagkey == "lanes"])
        # print(object[object.tagkey == "oneway"])

        #Check if the road has a name
        if(len(name_df) == 1): 
            name = name_df.tagvalue.item()
            #Check if there is already a road with the same name
            if(name in roadnames):
                num = 2
                newname = name +str(num)
                while(newname in roadnames):
                    num += 1
                    newname = name +str(num)
                roadnames.update({newname:x})
            else:
                roadnames.update({name:x})

def getbuildings():
    for way in osm.df_osm[osm.df_osm.tagkey == "building"].id:
        nodes_df = ws[ws.id == way]
        if(len(nodes_df)> 0):
            nodelist = nodes_df.nodes.item()
            buildings.update({way:nodelist})

osm_df = osm.df_osm
ws = osm.df_ways
getroads()
getbuildings()
