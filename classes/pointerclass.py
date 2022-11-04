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
        self.rect.center = pygame.mouse.get_pos() #moves the mouse to the mouses position (the center of ir)

    def createPlant(self, mousex, mousey, tilesize):
        x = mousex // tilesize #calculate where to place it, uses // to ensure plant fits in the square perfectly 
        y = mousey // tilesize
        squarecheck = True
        #checks if there is already a plant in the square
        for placed in plant_list:
            if placed.x == x and placed.y == y: 
                squarecheck == False
        if squarecheck == True: #Means the plant can be placed there
            plant = Plants(x, y, tilesize)
            plant_list.add(plant)
            all_sprites_list.add(plant)