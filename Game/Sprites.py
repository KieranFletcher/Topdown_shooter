from settings import *
import pygame


class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((30, 40))
        #width and height
        self.image.fill(255, 0, 0)

        self.rect = self.image.get_rect()

def new_game(self):
    #init the varibles for a new game.
    self.all_sprites = pygame.sprite.Group()
    self.run()
    self.player = Player()
    self.all_sprites.add(self.players)

def draw(self):
    self.all_sprites.draw(self.window)

def update(self):
    #update game loop
    self.all_sprites.update()