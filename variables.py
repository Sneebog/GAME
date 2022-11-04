import pygame
# Define some colors
WHITE = (255, 255, 255)
BLACK= (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (89, 61, 252)
#TILES
WIDTH=1000
HEIGHT=700
TILESIZE=100
GRIDWIDTH = WIDTH/TILESIZE  #  10 squares
GRIDHEIGHT = HEIGHT/TILESIZE # 7 squares
#timer variables
score = 0 
timerfps= 0
timer = 120
timersec = 0
timermin = 0
bullettimer = 0
wavenum = 1
#score and highscore variables
score = 0 
########make groups########
all_sprites_list = pygame.sprite.Group() #group for all objects
enemies_hit_list = pygame.sprite.Group() #group for all enemies that have been killed
bullets_hit_list = pygame.sprite.Group() #group for all enemies that have been killed
enemies_list = pygame.sprite.Group() #group for all enemies
plant_list = pygame.sprite.Group()#group for all plants
bullets_list = pygame.sprite.Group() #group for all bullets
heldplant = pygame.sprite.GroupSingle()
menu_sprites_list = pygame.sprite.Group() #group for all objects in menu
