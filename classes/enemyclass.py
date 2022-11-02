from classes.entityclass import Entity
from variables import RED, TILESIZE, enemies_hit_list
import pygame
class Enemies(Entity):
    def __init__(self, x, y , tilesize):
        super().__init__(x,y, tilesize)
        self.image.fill(RED)
        self.x_offset = (-0.005) #speed of the enemy, must be negative as the enemy always goes left
        self.health = 100 #total enemy health

    def damage(self,score ):
        self.health -= 20 
        if self.health <= 0:#if the enemy is zero health then it is killed 
            self.kill()
            score += 20 # for each enemy killed the score increases for the scoreboard
        return score

    def update(self):
        super().update()
        self.x += self.x_offset #make the enemy move at a constant speed

    def gameover(self):
        if self.x * TILESIZE < 30: #if the enemy reaches x = 30 then the game is over and the enemies won
            return True 