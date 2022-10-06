import pygame
from classes.backgroundclass import Background
from classes.bulletsclass import  Bullets
from classes.cameraclass import Camera
from  classes.enemyclass import Enemies
from  classes.plantclass import Plants
from  classes.pointerclass import Pointer
from variables import *
from os import path
#from camera import *
# Initialize the game engine
pygame.init()
 

# Set the height and width of the screen
size = (WIDTH, HEIGHT) # need a whole number of squares so wholly divisible by 32
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tower defense') 
icon = pygame.image.load('minionicon.jpg')
pygame.display.set_icon(icon)
game_folder=path.dirname(__file__)
map_data=[]
with open(path.join(game_folder, 'map.txt'), 'rt')as f:
    for line in f:
        map_data.append(line)       
pygame.key.set_repeat(500,100)  #lets held down key repeat

background = Background("gamebackground.jpg", [0,0])

camera=Camera(1,1)
#create fonts
outfit = pygame.font.SysFont('Outfit-Bold.ttf', 35)
#########make wall data##############
pointer = Pointer(RED, 20, 20)
all_sprites_list.add(pointer)
for row, tiles in enumerate(map_data):  #enumerate returns the index value of the item
    for col, tile in enumerate(tiles):  #enumerate returns the index value of the item
        if tile=="1":
            enemy=Enemies(col, row, TILESIZE)  #col will be the number of the column, row the number enumerated when the 1 is found
            all_sprites_list.add(enemy)
            enemies_list.add(enemy) #add wall to wall group
        if tile == "2":
            plant = Plants(col, row, TILESIZE)
            all_sprites_list.add(plant)
            plant_list.append(plant)
done = False
click = False
clock = pygame.time.Clock()
# Loop as long as done == False
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loo  
        if event.type == pygame.mouse.get_pressed:
            click = True
    screen.fill(WHITE)
    #set the background image
    screen.blit(background.image, background.rect)
    for x in range(0, WIDTH, TILESIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT)) #draws vertical lines every TILESIZE and going as far as HEIGHT down
    for y in range(0, HEIGHT, TILESIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y)) #draws horizontal lines every TILESIZE and going across as far as WIDTH
    #draw the scoreboards and the title
    score_board = outfit.render("SCORE: " +  str(score),  True, GREEN)
    Timer = outfit.render("TIME " +  str(timermin ) + ":" + str(timersec),  True, GREEN)
    #highscore_board = outfit.render("HIGHSCORE: " + str(6 * 12 * 20),  True, BLUE)
    screen.blit(score_board, (855, 60))
    screen.blit(Timer, (855, 80))
    all_sprites_list.update()
    for sprite in all_sprites_list:
        screen.blit(sprite.image, camera.apply(sprite))
    pos = pygame.mouse.get_pos()
    pointer.rect.x = pos[0]
    pointer.rect.y= pos[1]
    for enemie in enemies_list:
        enemie.move(-0.005)
    for bullet in bullets_list:
        bullet.move(0.01)
    for bullet in bullets_list:
        enemies_hit_list = pygame.sprite.spritecollide(bullet, enemies_list, True)
        if len(enemies_hit_list) > 0:
            bullet.kill()
    chimbus += 1
    if chimbus == 180:
        chimbus = 0
        for plant in plant_list:
            plant.shoot()
    timerfps += 1
    if timerfps == 60:
        timerfps = 0 
        timer -= 1
        timermin = timer // 60
        timersec = timer % 60
    pygame.display.flip()
    
    # Check the list of collisions
    clock.tick(60)
# Be IDLE friendly
pygame.quit()