from operator import truediv
import pygame
from classes.plantclass import Plants, Sunflowerplant
from variables import *
class Pointer(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        leaf = pygame.image.load('leafpointer.png').convert_alpha() # get the image for the pointer
        leaf = pygame.transform.scale(leaf, (width, height))
        self.image = leaf # apply lead to the pointer
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
    
    def update(self):
        self.rect.center = pygame.mouse.get_pos() #moves the mouse to the mouses position (the center of it)

    def createPlant(self, mousex, mousey, tilesize, type, money):
        x = mousex // tilesize #calculate where to place it, uses // to ensure plant fits in the square perfectly 
        y = mousey // tilesize
        squarecheck = True
        #checks if there is already a plant in the square
        
        for placed in plant_list: 
            if (placed.x == x) and (placed.y == y): 
                    squarecheck == False

        if x == 0 or y == 0: #ensures plants cant be placed on the top or the back line
            squarecheck = False

        if squarecheck == True: #Means the plant can be placed there
            if type == "peashooter": #if peashooter make normal plant
                if money >= 30: # if player can afford it then it is placed
                    money -= 30 # reduce the money
                    plant = Plants(x, y, tilesize)
                    plant_list.add(plant)
                    all_sprites_list.add(plant)
            elif type == "sunflower":  #if sundflower make sunflower plant
                if money > 15:# if player can afford it then it is placed
                    money -= 15 # reduce the money
                    sunflower = Sunflowerplant(x, y, tilesize)
                    plant_list.add(sunflower)
                    all_sprites_list.add(sunflower)
        return money