from classes.entityclass import Entity
from variables import RED, TILESIZE, enemies_hit_list
class Enemies(Entity):
    def __init__(self, x, y , tilesize):
        super().__init__(x,y, tilesize)
        self.image.fill(RED)
        self.x_offset = (-0.005)
    
    def update(self):
        super().update()
        self.x += self.x_offset
        if enemies_hit_list:   
            self.kill()
    def gameover(self):
        if self.x * TILESIZE < 30:
            return True