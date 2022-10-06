import pygame
# Define some colors
WHITE = (255, 255, 255)
BLACK= (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
#TILES
WIDTH=1000
HEIGHT=700
TILESIZE=100
GRIDWIDTH = WIDTH/TILESIZE  #  10 squares
GRIDHEIGHT = HEIGHT/TILESIZE # 7 squares
#funny variables
chimbus = 0
score = 0 
timerfps= 0
timer = 120
timersec = 0
timermin = 0
########make groups########

all_sprites_list = pygame.sprite.Group() #group for all objects
enemies_hit_list = pygame.sprite.Group()
enemies_list = pygame.sprite.Group()
plant_list = []
bullets_list = pygame.sprite.Group()