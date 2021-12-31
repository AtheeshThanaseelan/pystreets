import os

# set the path before raylib is imported.
os.environ["RAYLIB_BIN_PATH"] = "__main__"

import raylibpy as rl
from ctypes import byref
import ctypes
MAX_COLUMNS = 20

# Define the camera to look into our 3d world
camera = rl.Camera(
    rl.Vector3(4.0, 2.0, 4.0),
    rl.Vector3(0.0, 0.0, 0.0),
    rl.Vector3(0.0, 1.0, 0.0),
    45.0,
    rl.CAMERA_PERSPECTIVE
)

gfx_cubes = []
gfx_lines = []

class cube():
    def __init__(self):
        self.pos = rl.Vector3(0.0, 0.0, 0.0)
        self.xsize = 1
        self.ysize = 1
        self.zsize = 1
        self.bcolor = rl.RED
        self.lcolor = rl.RAYWHITE

class line():
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.z1 = 0
        self.x2 = 0
        self.y2 = 0
        self.z2 = 0
        self.lcolor = rl.RED

def setup_gfx():
    # Initialization
    # ---------------------------------------------------------------
    screen_width = 800
    screen_height = 600

    rl.init_window(screen_width, screen_height, "raylib")

    rl.set_camera_mode(camera, rl.CAMERA_FREE)
    rl.set_camera_alt_control(rl.KEY_A)
    rl.set_target_fps(60)    

def loop():
        # Update
        # -----------------------------------------------------------
        rl.update_camera(byref(camera))
        if rl.is_key_down(rl.KEY_Z):
            camera.target = rl.Vector3(0.0, 0.0, 0.0)
        # -----------------------------------------------------------

        # Draw
        # -----------------------------------------------------------
        rl.begin_drawing()

        rl.clear_background(rl.RAYWHITE)

        rl.begin_mode3d(camera)

        for x in gfx_lines:
            #print(x.x1)
            rl.draw_line3_d(rl.Vector3(x.x1,x.y1,x.z1),rl.Vector3(x.x2,x.y2,x.z2),x.lcolor)


        for x in gfx_cubes:
            rl.draw_cube(x.pos,x.xsize,x.ysize,x.zsize,x.bcolor)
            rl.draw_cube_wires(x.pos,x.xsize,x.ysize,x.zsize,x.lcolor)

        rl.draw_grid(1000, 1.0)

        rl.end_mode3d()

        rl.draw_rectangle(10, 10, 320, 133, rl.fade(rl.SKYBLUE, 0.5))
        rl.draw_rectangle_lines(10, 10, 320, 133, rl.BLUE)
        
        rl.draw_text("Free camera default controls:", 20, 20, 10, rl.BLACK)
        rl.draw_text("- Mouse Wheel to Zoom in-out", 40, 40, 10, rl.DARKGRAY)
        rl.draw_text("- Mouse Wheel Pressed to Pan", 40, 60, 10, rl.DARKGRAY)
        rl.draw_text("- Alt + Mouse Wheel Pressed to Rotate", 40, 80, 10, rl.DARKGRAY)
        rl.draw_text("- Alt + Ctrl + Mouse Wheel Pressed for Smooth Zoom", 40, 100, 10, rl.DARKGRAY)
        rl.draw_text("- Z to Zoom to (0, 0, 0)", 40, 120, 10, rl.DARKGRAY)

        rl.end_drawing()

def quit_gfx():
    # De-Initialization
    # ---------------------------------------------------------------
    rl.close_window()       # Close window and OpenGL context
    # ---------------------------------------------------------------


#setup_gfx()

#while(True):
    loop()

#quit_gfx()