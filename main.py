import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SHOWN)
    timer = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    return

        updatable.update(dt)

        for ast in asteroids:
            for shot_ast in shots:
                if ast.collision(shot_ast):
                    ast.split()
                    shot_ast.kill()
            if ast.collision(player):
                print("Game Over!")
                sys.exit()

        screen.fill((0, 0, 0), rect=None, special_flags=0)

        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        dt = timer.tick(60) / 1000


if __name__ == "__main__":
    main()
