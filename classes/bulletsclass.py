from classes.entityclass import Entity #inherits from entity 
import pygame
from variables import TILESIZE, RED, enemies_hit_list, enemies_list, bullets_hit_list
class Bullets(Entity):
    def __init__(self, x, y , width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.width = width
        self.height = height
        self.image.fill(RED) #colour of the bullet
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.x_offset = 0.01 #offset is the speed that the bullet will move at

    def update(self):
        self.rect.x=self.x*TILESIZE  #multiply the x and y by tilesize to draw on screen
        self.rect.y=(self.y*TILESIZE) + 50
        self.x += self.x_offset #make the bullet move at a constant speed

class SunBullets(Bullets):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.startx = self.x
        self.starty = self.y 
        self.x_offset = 0.01
        self.y_offset = -0.02
        self.yflag = False
        self.xflag = False
        self.timer = 0
        
    def update(self):
        self.rect.x=self.x*TILESIZE  #multiply the x and y by tilesize to draw on screen
        self.rect.y=(self.y*TILESIZE) + 50
        #make the sun move up then down, uses the flags to stop it moving and to change directions
        if self.x <= (self.startx + 1.5):
            self.x += self.x_offset
        else:
            self.xflag = True

        if self.xflag == False:
            if (self.y >= (self.starty - 1.5)) and self.yflag == False:
                self.y += self.y_offset
            else:
                self.yflag = True
                self.y -= self.y_offset / 2
        #timer for the lifespan of the sun
        self.timer += 1
