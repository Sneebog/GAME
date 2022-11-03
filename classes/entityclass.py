from variables import WHITE, TILESIZE
import pygame
class Entity(pygame.sprite.Sprite): #creation of a class used as a base for other sprites to inherit from
    def __init__(self, x, y, TILESIZE):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(WHITE)
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        
    def update(self):
        self.rect.x=self.x*TILESIZE   #multiply the x and y by tilesize to draw on screen
        self.rect.y=self.y*TILESIZE