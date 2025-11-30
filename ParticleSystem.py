import pygame
from Particle import Particle
import random
from settings import *

class ParticleSystem():
    def __init__(self, x_, y_, world):
        self.origin = (x_, y_)
        self.world = world

        self.particles = []

        self.age = 1

    def update_origin(self, origin):
        self.origin = origin.get()

    def addParticle(self):
        p1 = Particle(self.origin[0], self.origin[1], self.world)
        p2 = Particle(self.origin[0]+random.uniform(-1, 1), self.origin[1]+random.uniform(-1, 1), self.world)
        self.particles.append(p1)
        self.particles.append(p2)

        self.world.CreateDistanceJoint(
            bodyA = p1.body,
            bodyB = p2.body,
            anchorA = p1.body.worldCenter,
            anchorB = p2.body.worldCenter,
            length = scalarPixelsToWorld(10 ),
            frequencyHz = 0,
            dampingRatio = 0
        )

    def run(self):
        self.age+=1

        for p in self.particles:
            p.display()

        self.particles = [p for p in self.particles if not p.isDead()]

    def isDead(self):
        if self.age>500:
            return True
        else:
            return False
