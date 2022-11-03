from classes.entityclass import Entity
from variables import all_sprites_list, bullets_list, RED
from classes.bulletsclass import Bullets

class Plants(Entity):
    def __init__(self, x, y , tilesize):
        super().__init__(x,y, tilesize)
        self.image.fill(RED)
        self.bullettimer = 180 #Timer for the plant to constantly shoot bullet
        self.health = 100 # total health for the plant 

    def damage(self):
        self.health -= 20 
        print(self.health)
        if self.health <= 0: #if the plant is zero health then it dies
            self.kill() 

    def update(self):
        super().update()
        # self.bullettimer -= 1
        # #shooting fucntion doesnt work rn
        # if self.bullettimer == 0 :
        #     print("bullet shot")
        #     self.bullettimer = 180
        #     bullet = Bullets(self.x, self.y, 5, 5)  #bullets are created at the plants position
        #     all_sprites_list.add(bullet)
        #     bullets_list.add(bullet)
           

    def shoot(self):
        #bullets creation
        bullet = Bullets(self.x, self.y, 5, 5) #bullets are created at the plants position   
        all_sprites_list.add(bullet)
        bullets_list.add(bullet)