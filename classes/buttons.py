import pygame
from variables import *
class buttons(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
        self.rect=self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        self.rect.x=self.x
        self.rect.y=self.y