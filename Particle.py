import math

import pygame
from Box2D.b2 import vec2, polygonShape
from settings import *

import random

class Particle():
    def __init__(self, x_, y_, world):
        self.x = x_
        self.y = y_

        self.w = 7
        self.h = 7

        self.lifespan = 255

        self.display_surface = pygame.display.get_surface()


        self.body = world.CreateDynamicBody(
            position = pixelsToWorld((self.x, self.y))
        )

        box2dW = scalarPixelsToWorld(self.w/2)
        box2dH = scalarPixelsToWorld(self.h/2)

        ps = polygonShape(
            box = (box2dW, box2dH)
        )

        self.body.CreateFixture(
            shape = ps,
            density = 1,
            friction = 0.3,
            restitution=0.5
        )

        init_force = vec2(random.uniform(-2, 2), random.uniform(-1, 0))
        self.applyForce(init_force)


    def applyForce(self, force):

        force = vec2(force)
        self.body.ApplyLinearImpulse(force, self.body.worldCenter, wake=True)


    def display(self):
        color= (175, 175, 175)
        border = (255, 255, 255)
        self.lifespan-=1

        rect_surface = pygame.Surface((self.w, self.h), pygame.SRCALPHA)

        pygame.draw.rect(rect_surface, color, (0, 0, self.w, self.h))
        pygame.draw.rect(rect_surface, border, (0, 0, self.w, self.h), 1)

        angle_degrees = -math.degrees(self.body.transform.angle)

        rotated_surface = pygame.transform.rotate(rect_surface, angle_degrees)

        rotated_rect = rotated_surface.get_rect(center=worldToPixels(self.body.transform.position))

        self.display_surface.blit(rotated_surface, rotated_rect)


    def isDead(self):
        if self.lifespan<0:
            return True
        else:
            return False