from settings import *
import pygame


class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((30, 40))
        #width and height
        self.image.fill(RED)

        self.rect = self.image.get_rect()

    def moveLeft(self):
        self.rect.x -= 5

    def moveRight(self):
        self.rect.x += 5

    def moveDown(self):
        self.rect.y += 5

    def moveUp(self):
        self.rect.y -= 5

class enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((30, 30))
        #width and height
        self.image.fill(WEIRD1)

        self.rect = self.image.get_rect()