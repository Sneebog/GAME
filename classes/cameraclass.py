from variables import WIDTH, HEIGHT
import pygame
class Camera:
    def __init__(self, width, height):
        self.camera=pygame.Rect(0,0, width, height)
        self.width=width
        self.height=height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH/2)
        y = -target.rect.y + int(HEIGHT/2)
        x=min(0,x) #stops going off on left
        y=min(0,y) #stops going off on top
       # x=max(-1024-2080,x)
        x=max(-(2080-1024),x)
        y=max(-(800-HEIGHT),y)
        
        self.camera = pygame.Rect(x, y, self.width, self.height)