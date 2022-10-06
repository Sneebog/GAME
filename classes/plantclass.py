from classes.entityclass import Entity
from variables import all_sprites_list, bullets_list, RED
from classes.bulletsclass import Bullets
class Plants(Entity):
    def __init__(self, x, y , tilesize):
        super().__init__(x,y, tilesize)
        self.image.fill(RED)
    def update(self):
        super().update()
    def shoot(self):
        bullet = Bullets(self.x, self.y, 5, 5)  
        all_sprites_list.add(bullet)
        bullets_list.add(bullet)