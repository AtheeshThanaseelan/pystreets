import os
import ctypes
# set the path before raylib is imported.
os.environ["RAYLIB_BIN_PATH"] = "__main__"
import raylibpy as rl
from ctypes import byref
MAX_COLUMNS = 20

# Define the camera to look into our 3d world
camera = rl.Camera(
    rl.Vector3(4.0, 2.0, 4.0),
    rl.Vector3(0.0, 0.0, 0.0),
    rl.Vector3(0.0, 1.0, 0.0),
    45.0,
    rl.CAMERA_PERSPECTIVE
)


screen_width = 800
screen_height = 600

rl.init_window(screen_width, screen_height, "raylib")

rl.set_camera_mode(camera, rl.CAMERA_FREE)
rl.set_camera_alt_control(rl.KEY_A)
rl.set_target_fps(60)   

mesh2 = rl.gen_mesh_plane(2.0,2.0,1,1)
mesh = rl.load_mesh("new.obj")
model = rl.load_model_from_mesh(mesh)


while(True):
    rl.update_camera(byref(camera))
    rl.begin_drawing()
    rl.clear_background(rl.RAYWHITE)
    rl.begin_mode3d(camera)


    rl.draw_model(model,rl.Vector3(0,0,0),1,rl.RED)

    rl.draw_grid(10, 1.0)
    rl.end_mode3d()
    rl.end_drawing()