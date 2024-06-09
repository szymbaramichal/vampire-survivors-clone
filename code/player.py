import pygame
from settings import *
from os.path import join

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player', 'down', '0.png')).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
    
        # Movement
        self.direction = pygame.Vector2(0, 0)
        self.speed = 500

    def input(self):
        keys = pygame.key.get_pressed()

        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

        # Normalize the direction vector if it's not zero
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()

        # Debugging output
        print(f"Direction: {self.direction}")

    def move(self, dt):
        # Update position based on direction and speed
        if self.direction.length() > 0:
            self.rect.center += self.direction * self.speed * dt

        # Debugging output
        print(f"Position: {self.rect.center}")

    def update(self, dt):
        self.input()
        self.move(dt)