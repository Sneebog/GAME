import random
from variables import *
from classes.enemyclass  import Enemies 
def spawnnewwave(framenum ):
    for i in range(0, wavenum):
        spawnnum = random.randint(1, 7) #what row they will spawn in 
        checknum = random.randint(1,12) #random chance for them to spawn
        if (framenum / 12) == checknum:
            enemy= Enemies(10, spawnnum, TILESIZE)#col will be the number of the column, row the number enumerated when the 1 is found
            all_sprites_list.add(enemy)
            enemies_list.add(enemy) #add enemy to enemies group

