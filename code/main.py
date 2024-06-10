import pygame
from settings import *
from player import Player
from sprites import *
from pytmx.util_pygame import load_pygame

from random import randint

class Game:
    def __init__(self):
        # Setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Vampire Survivor clone')
        self.clock = pygame.time.Clock()
        self.running = True

        # Groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.setup()
        #sprites
        self.player = Player((400, 300), self.all_sprites, self.collision_sprites)

    def run(self):
        while self.running:
            # Delta time in seconds
            dt = self.clock.tick(60) / 1000

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Update
            self.all_sprites.update(dt)

            # Draw
            self.display_surface.fill((0, 0, 0))  # Clear the screen with a black color
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()

        pygame.quit()

    def setup(self):
        map = load_pygame(join('data', 'maps', 'world.tmx'))
        
        for x,y,image in map.get_layer_by_name('Ground').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)
                    
        for obj in map.get_layer_by_name('Objects'):
            CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))

        for obj in map.get_layer_by_name('Collisions'):
            CollisionSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprites)

if __name__ == '__main__':
    game = Game()
    game.run()