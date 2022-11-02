from classes.entityclass import Entity #inherits from entity 
import pygame
from variables import TILESIZE, RED, enemies_hit_list, enemies_list, bullets_hit_list
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
        self.x_offset = 0.01
    def update(self):
        self.rect.x=self.x*TILESIZE  #multiply the x and y by tilesize to draw on screen
        self.rect.y=(self.y*TILESIZE) + 50
        self.x += self.x_offset #make the bullet move at a constant speed
        # enemies_hit_list = pygame.sprite.spritecollide(self, enemies_list, True)
        # print(enemies_hit_list)