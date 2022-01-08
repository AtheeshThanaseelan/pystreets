import osmium as osm
import pandas as pd
import math
import numpy as np
import os

scale = 100

def cordtoint(cord):
    i = cord.index('/')
    lon = float(cord[0:i])
    lat = float(cord[i+1:len(cord)])
    return [lat,lon]

class OSMHandler(osm.SimpleHandler):
    def __init__(self):
        osm.SimpleHandler.__init__(self)
        self.osm_data = []
        self.node_loc = []
        self.way_ns = []
        self.rels = []

    def tag_inventory(self, elem, elem_type):
        for tag in elem.tags:
            #print(tag)
            self.osm_data.append([elem_type, 
                                   elem.id, 
                                   elem.version,
                                   elem.visible,
                                   pd.Timestamp(elem.timestamp),
                                   elem.uid,
                                   elem.user,
                                   elem.changeset,
                                   len(elem.tags),
                                   tag.k, 
                                   tag.v])

    def node(self, n):
        loc = []
        loc.append(int(n.id))
        loc.append(cordtoint(str(n.location)))
        self.node_loc.append(loc)
        self.tag_inventory(n, "node")

    def way(self, w):
        nodes = []
        way = []
        for x in w.nodes:
            nodes.append(int(str(x)))
        way.append(int(w.id))
        way.append(nodes)
        self.tag_inventory(w, "way")
        self.way_ns.append(way)

    def relation(self, r):
        #rel = []
        #print(dir(r))
        #print(r)
        self.tag_inventory(r, "relation")

def getlocs(dway,dnode,id):
    way = df_ways[df_ways.id == id]
    cords = []
    for n in way.nodes.item():
        node = df_nodes[df_nodes.id == n]
        cord = node.location.item() 
        cords.append((cord))
    return cords

def latlontocart(cord):
    #x = 6371* 10 * math.cos(cord[0]) * math.cos(cord[1])
    #y = 6371* 10 * math.cos(cord[0]) * math.sin(cord[1])
    #z = 6371* 10 * math.sin(cord[0])
    lat, lon = np.deg2rad(cord[0]), np.deg2rad(cord[1])
    R = 6371 # radius of the earth
    x = R * np.cos(lat) * np.cos(lon) * scale * -1
    y = R * np.cos(lat) * np.sin(lon) * scale
    z = R *np.sin(lat)
    #print(x,y,z)
    return [x,y,z]#

def localize(cord):
    b = df_nodes
    t = 0
    loc = b.at[0,'location']
    if(str(type(loc)) != "<class 'list'>"):
        t = t+1
        loc = b.at[t,'location']

    norm = latlontocart(loc)
    
    x_o = norm[0]#852.2245421338656 * scale
    y_o = norm[1]#-4525.177344212292 * scale
    z_o = 4402.967673423517 * 1
    xn = cord[0] - x_o
    yn = cord[1] - y_o
    zn = 0#cord[2] - z_o
    return [xn,yn,zn]

def getpont(cord):
    return localize(latlontocart(cord))

def nodetocords(nodeid):
    node = df_nodes[df_nodes.id == nodeid]
    cord = node.location.item() 
    return cord

df_osm = 0
df_nodes = 0
df_ways = 0
base = "working/"
if((1==1)&(os.path.isfile(base+"tags.pkl") & os.path.isfile(base+"nodes.pkl") & os.path.isfile(base+"ways.pkl"))):
    df_osm = pd.read_pickle(base+"tags.pkl")
    df_nodes = pd.read_pickle(base+"nodes.pkl")
    df_ways = pd.read_pickle(base+"ways.pkl")
else:
    osmhandler = OSMHandler()
    # scan the input file and fills the handler list accordingly
    osmhandler.apply_file(base+"map.osm")

    # transform the list into a pandas DataFrame
    data_colnames = ['type', 'id', 'version', 'visible', 'ts', 'uid',
                    'user', 'chgset', 'ntags', 'tagkey', 'tagvalue']
    df_osm = pd.DataFrame(osmhandler.osm_data, columns=data_colnames)

    data_colnames = ['id','location']
    df_nodes = pd.DataFrame(osmhandler.node_loc,columns=data_colnames)

    data_colnames = ['id','nodes']
    df_ways = pd.DataFrame(osmhandler.way_ns,columns=data_colnames)

    df_osm.to_pickle(base+"tags.pkl")
    df_nodes.to_pickle(base+"nodes.pkl")
    df_ways.to_pickle(base+"ways.pkl")

if __name__ == "__main__":

    

    print(df_osm[df_osm.tagkey == "highway"].id)  

    #for way in df_osm[df_osm.tagkey == "building"].id:
    #for way in df_ways.id:
    #    print(way)

    #for x in df_ways.id:
    #    print(x)
    #print(df_nodes[df_nodes.id == '31363751'])
    #print(df_osm[df_osm.tagvalue == 'Grenoble Drive'])
    #print(df_osm[(df_osm.tagvalue == '10') & (df_osm.tagkey == 'addr:housenumber')])
