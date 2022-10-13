from operator import truediv
import pygame
from classes.plantclass import Plants
from variables import *
class Pointer(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
    def createPlant(self, mousex, mousey, tilesize):
        x = mousex // tilesize
        y = mousey // tilesize
        squarecheck = True
        for placed in plant_list:
            if placed.x == x and placed.y == y:
                squarecheck == False
        if squarecheck == True:
            plant = Plants(x, y, tilesize)
            all_sprites_list.add(plant)
            plant_list.append(plant)