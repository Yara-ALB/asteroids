import pygame
from circleshape import CircleShape

class Shot(CircleShape) :
    def __init__(self, position, velocity, radius):
        super().__init__(position.x, position.y, radius)
        pygame.sprite.Sprite.__init__(self)
        self.velocity = velocity
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, width=2)

    def update(self, dt):
        self.position.x = self.position.x + (self.velocity.x * dt)
        self.position.y = self.position.y + (self.velocity.y * dt)
        