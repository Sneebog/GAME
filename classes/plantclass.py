from classes.entityclass import Entity
from variables import all_sprites_list, bullets_list, WHITE, PURPLE, sunbullets_list
from classes.bulletsclass import Bullets, SunBullets
import random
import pygame


class Plants(Entity):
    def __init__(self, x, y , tilesize,):
        super().__init__(x,y, tilesize)
        peashooter = pygame.image.load('Peashooter.jpg').convert_alpha() #get the image of the plant
        peashooter = pygame.transform.scale(peashooter, (tilesize, tilesize))
        self.image.set_colorkey(WHITE)
        self.image = peashooter
        self.bullettimer = random.randint(0, 180) #Timer for the plant to constantly shoot bullet
        self.health = 100 # total health for the plant 
        self.timer = 0
    def damage(self):
        self.health -= 5
        if self.health <= 0: #if the plant is zero health then it dies
            self.kill() 
      
    def update(self):
        super().update()
        self.timer += 1 #increase the timer
        self.image
           

    def shoot(self):
        #bullets creation
        #bullet = Bullets(self.x + 0.5, self.y, 10, 10) #bullets are created at the plants position
        bullet = Bullets(self.x + 1, self.y, 10, 10)
        all_sprites_list.add(bullet)
        bullets_list.add(bullet)
        self.timer = 0

class Sunflowerplant(Plants):
    def __init__(self, x, y, tilesize):
        super().__init__(x, y, tilesize) #inherit basic attributes of the plant
        sunflower = pygame.image.load('flower.png').convert_alpha()
        sunflower = pygame.transform.scale(sunflower, (tilesize, tilesize))
        self.image = sunflower #crete the sunflower sprite
    
    def damage(self):
       super().damage() #inheirt the function from the plant class
    
    def shoot(self):
        #sun creation 
        sun = SunBullets(self.x, self.y, 10, 10)
        all_sprites_list.add(sun)
        sunbullets_list.add(sun)
        self.timer = 0