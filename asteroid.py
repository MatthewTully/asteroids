from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):

    containers: set

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity*dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        self.spawn(5)
    
    def spawn(self, num):
        
        new_vectors = []
        for i in range(0, num):
            angle = random.uniform(-50,50)
            new_vectors.append(self.velocity.rotate(angle))
        new_size = self.radius - ASTEROID_MIN_RADIUS
        for new in new_vectors:
            new_roid = Asteroid(self.position.x, self.position.y, new_size)
            new_roid.velocity = new * 1.2
        
