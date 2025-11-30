# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
import Box2D
from Box2D.b2 import world
import sys
from settings import *
from Particle import Particle
from ParticleSystem import ParticleSystem

pygame.init()

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("body particles")

clock = pygame.time.Clock()

world = world(gravity = (0, -10), doSleep = True)

psystems = []

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    display_surface.fill((0,0,0))

    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        ps = ParticleSystem(x, y, world)
        psystems.append(ps)


    for ps in psystems:
        if not ps.isDead():
            ps.addParticle()
            ps.run()
        else:
            print(ps.age)
            psystems = [ps for ps in psystems if not ps.isDead()]

    world.Step(STEP, 6, 10)
    clock.tick(TARGET_FPS)
    pygame.display.update()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
