import pygame
# Define some colors
WHITE = (255, 255, 255)
BLACK= (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (89, 61, 252)
GREY = (178, 190, 181)
ORANGE = (235, 102, 7)
PROPERPURP = (156, 9, 230)
BLUE = (0,0,255)
#TILES
WIDTH=1000
HEIGHT=700
TILESIZE=100
GRIDWIDTH = WIDTH/TILESIZE  #  10 squares
GRIDHEIGHT = HEIGHT/TILESIZE # 7 squares
wavenum = 1
########make groups########
all_sprites_list = pygame.sprite.Group() #group for all objects
enemies_hit_list = pygame.sprite.Group() #group for all enemies that have been killed
bullets_hit_list = pygame.sprite.Group() #group for all enemies that have been killed
background_list = pygame.sprite.Group()
enemies_list = pygame.sprite.Group() #group for all enemies
plant_list = pygame.sprite.Group()#group for all plants
bullets_list = pygame.sprite.Group() #group for all bullets
heldplant = pygame.sprite.GroupSingle()
menu_sprites_list = pygame.sprite.Group() #group for all objects in menu
sunbullets_list = pygame.sprite.Group() #group for all sun 
pointer_list = pygame.sprite.Group()