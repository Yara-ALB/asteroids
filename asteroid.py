import random
import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(
            screen, (255, 255, 255), (self.x, self.y), self.radius, width=2
        )

    def update(self, dt):
        self.x = self.x + (self.velocity.x * dt)
        self.y = self.y + (self.velocity.y * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        randAngle = random.uniform(20, 50) 
        velocity_vector_1 = self.velocity.rotate(randAngle)
        velocity_vector_2 = self.velocity.rotate(-randAngle)
        self.new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, self.new_radius)
        asteroid_1.velocity = velocity_vector_1 * 1.2
        asteroid_2 = Asteroid(self.position.x, self.position.y, self.new_radius)
        asteroid_2.velocity = velocity_vector_2 * 1.2