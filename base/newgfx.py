from distutils.sysconfig import customize_compiler
import os
from turtle import update

# set the path before raylib is imported.
os.environ["RAYLIB_BIN_PATH"] = "working/"

import raylibpy as rl
from ctypes import byref
import ctypes
MAX_COLUMNS = 20
import pickle

# Define the camera to look into our 3d world
camera = 0



def setup_gfx():
    # Initialize variables
    # ---------------------------------------------------------------
    global camera
    screen_width = 800
    screen_height = 600
    if(os.path.isfile("working/save.sav")):
        f = open("working/save.sav","rt")
        cam = f.read()
        camlist = cam.split("\n")
        #print(camlist)
        camera = rl.Camera(
            rl.Vector3(float(camlist[0]),float(camlist[1]),float(camlist[2])),
            rl.Vector3(float(camlist[3]),float(camlist[4]),float(camlist[5])),
            rl.Vector3(float(camlist[6]),float(camlist[7]),float(camlist[8])),
            45.0,
            rl.CAMERA_PERSPECTIVE
        )
    else:
        #print("NO")
        camera = rl.Camera(
            rl.Vector3(4.0, 2.0, 4.0),
            rl.Vector3(0.0, 0.0, 0.0),
            rl.Vector3(0.0, 1.0, 0.0),
            45.0,
            rl.CAMERA_PERSPECTIVE
        )

    rl.init_window(screen_width, screen_height, "raylib")
    rl.set_camera_mode(camera, rl.CAMERA_FREE)
    rl.set_camera_alt_control(rl.KEY_A)
    rl.set_target_fps(60)    

def quit_gfx():
    #Save info
    caminfo = []
    caminfo.append(str(camera.position[0]))
    caminfo.append(str(camera.position[1]))
    caminfo.append(str(camera.position[2]))
    caminfo.append(str(camera.target[0]))
    caminfo.append(str(camera.target[1]))
    caminfo.append(str(camera.target[2]))
    caminfo.append(str(camera.up[0]))
    caminfo.append(str(camera.up[1]))
    caminfo.append(str(camera.up[2]))
    caminfo.append(str(camera.fovy))
    caminfo.append(str(camera.type))
        
    objFile = open("working/save.sav", 'w')
    for x in caminfo:
        objFile.write(x+"\n")
    objFile.close() 
    # De-Initialization
    # ---------------------------------------------------------------
    rl.close_window()       # Close window and OpenGL context
    # ---------------------------------------------------------------

class gfxframe():
    def __init__(self):
        self.custom_funcs = []
        setup_gfx()

    def loop(self):
        # Update
        # -----------------------------------------------------------
        rl.update_camera(byref(camera))
        if rl.is_key_down(rl.KEY_Z):
            camera.target = rl.Vector3(0.0, 0.0, 0.0)
        # -----------------------------------------------------------

        # Draw
        rl.begin_drawing()
        rl.clear_background(rl.SKYBLUE)
        rl.begin_mode3d(camera)

        

        #Custom 3D function
        for func in self.custom_funcs:
            func()

        rl.end_mode3d()


        #2D Drawing
        rl.draw_rectangle(10, 10, 320, 133, rl.fade(rl.SKYBLUE, 0.5))
        rl.draw_rectangle_lines(10, 10, 320, 133, rl.BLUE)
        rl.draw_text("Free camera default controls:", 20, 20, 10, rl.BLACK)
        rl.draw_text("- Mouse Wheel to Zoom in-out", 40, 40, 10, rl.DARKGRAY)
        rl.draw_text("- Mouse Wheel Pressed to Pan", 40, 60, 10, rl.DARKGRAY)
        rl.draw_text("- Alt + Mouse Wheel Pressed to Rotate", 40, 80, 10, rl.DARKGRAY)
        rl.draw_text("- Alt + Ctrl + Mouse Wheel Pressed for Smooth Zoom", 40, 100, 10, rl.DARKGRAY)
        rl.draw_text("- Z to Zoom to (0, 0, 0)", 40, 120, 10, rl.DARKGRAY)
        rl.end_drawing()


        keepopen = not rl.window_should_close() 

        if not keepopen:
            quit_gfx()

        return keepopen

gfx_cubes = []
gfx_lines = []
models = []

class cube():
    def __init__(self):
        self.pos = rl.Vector3(0.0, 0.0, 0.0)
        self.xsize = 1
        self.ysize = 1
        self.zsize = 1
        self.bcolor = rl.RED
        self.lcolor = rl.RAYWHITE
    def setpos(self,x,y,z):
        self.pos = rl.Vector3(x,y,z)

class line():
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.z1 = 0
        self.x2 = 0
        self.y2 = 0
        self.z2 = 0
        self.lcolor = rl.BLACK

def load_buildings():
    base = "working/"
    for x in os.listdir(base+"objs/buildings/"):
        mesh = rl.load_mesh(base+"objs/buildings/"+x)
        model = rl.load_model_from_mesh(mesh)
        models.append(model)

def load_streets():
    for x in os.listdir("working/objs/streets/"):
        mesh = rl.load_mesh("working/objs/streets/"+x)
        model = rl.load_model_from_mesh(mesh)
        models.append(model)

def gfxlineupdate():
    for x in gfx_lines:
        # print(x.x1)
        rl.draw_line3_d(rl.Vector3(x.x1,x.y1,x.z1),rl.Vector3(x.x2,x.y2,x.z2),x.lcolor)

def gfxcubeupdate():
    for x in gfx_cubes:
        rl.draw_cube(x.pos,x.xsize,x.ysize,x.zsize,x.bcolor)
        rl.draw_cube_wires(x.pos,x.xsize,x.ysize,x.zsize,x.lcolor)

def gfxmodelupdate():
    
    for x in models:
        rl.draw_model(x,rl.Vector3(0,0,0),1,rl.BLUE)
        rl.draw_model_wires(x,rl.Vector3(0,0,0),1,rl.BLACK)


locmap = {}
modelmap = {}

def loadmodelloc():
    base = "working/"
    
    for x in os.listdir(base+"locs/buildings/"):
        id = x.split('.')[0]
        with open(base+'locs/buildings/'+x, 'rb') as f:
            loc = pickle.load(f)
            locmap.update({id:loc})
        mesh = rl.load_mesh(base+"objs/buildings/"+id+".obj")
        model = rl.load_model_from_mesh(mesh)
        modelmap.update({id:model})


def camgrid():
#3D Drawing
    campos = camera.position
    rl.draw_grid(1000, 1.0)
    rl.draw_plane(rl.Vector3(campos[0],-0.5,campos[2]),rl.Vector2(1000,1000),rl.WHITE)

def gfxlocmodelupdate(): 
    load = []
    campos = camera.position

    for id in locmap:
        loc = locmap[id]
        x_compare = campos[0] - loc[0]
        x_compare = abs(x_compare)
        z_compare = campos[2] - loc[2]
        z_compare = abs(z_compare)
        if((x_compare < 300) & (z_compare < 300)):
            load.append(id)
            rl.draw_model(modelmap[id],rl.Vector3(locmap[id][0],locmap[id][1],locmap[id][2]),1,rl.BLUE)
            rl.draw_model_wires(modelmap[id],rl.Vector3(locmap[id][0],locmap[id][1],locmap[id][2]),1,rl.BLACK)
        # print(loc)
        # print(campos)
        # print("\n\n\n\n")        

    #Load all: replace load with modelmap
    # for id in load:
        # print(modelmap[id])
        