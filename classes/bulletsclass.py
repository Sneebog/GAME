from classes.entityclass import Entity
import pygame
from variables import TILESIZE, RED
class Bullets(Entity):
    def __init__(self, x, y , width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.width = width
        self.height = height
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
    def update(self):
        self.rect.x=self.x*TILESIZE  #multiply the x and y by tilesize to draw on screen
        self.rect.y=(self.y*TILESIZE) + 50
    def move(self, x_offset):
        self.x += x_offset