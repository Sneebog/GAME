from classes.entityclass import Entity
from variables import RED
class Enemies(Entity):
    def __init__(self, x, y , tilesize):
        super().__init__(x,y, tilesize)
        self.image.fill(RED)
    def update(self):
        super().update()
    def move(self, x_offset):
        self.x += x_offset   