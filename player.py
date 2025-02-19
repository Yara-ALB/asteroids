import pygame

from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_SHOOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
    SHOT_RADIUS,
    PLAYER_SHOOT_COOLDOWN
)
from shot import Shot


class Player(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, shots_group):
        super().__init__(x, y, PLAYER_RADIUS)
        pygame.sprite.Sprite.__init__(self)
        self.radius = PLAYER_RADIUS

        self.timer = 0
        self.rotation = 0
        self.image = pygame.Surface(
            (PLAYER_RADIUS * 2, PLAYER_RADIUS * 2), pygame.SRCALPHA
        )
        self.rect = self.image.get_rect(center=(x, y))
        self.shots_group = shots_group

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), width=2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        position = self.position
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        new_shot = Shot(self.position, velocity, SHOT_RADIUS)
        self.shots_group.add(new_shot)
        self.timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        self.timer -= dt
        if self.timer > 0:
            self.button_pressed = False
        else:
            self.button_pressed = True
        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_z]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.button_pressed :
                self.shoot()
