

WIDTH = 1920
HEIGHT = 1080

PPM = 30.0

TARGET_FPS = 60

STEP = 1/TARGET_FPS

def pixelsToWorld(P):
    world_x = P[0]/PPM
    world_y = (-P[1]+HEIGHT)/PPM
    return world_x, world_y

def worldToPixels(P):
    screen_x = P[0]*PPM
    screen_y = -P[1]*PPM +HEIGHT
    return screen_x, screen_y

def scalarPixelsToWorld(val):
    return val/PPM

