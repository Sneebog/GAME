from operator import truediv
import pygame
from classes.backgroundclass import Background
from classes.bulletsclass import  Bullets
from classes.cameraclass import Camera
from  classes.enemyclass import Enemies
from  classes.plantclass import Plants
from  classes.pointerclass import Pointer
#all the classes imported
from variables import *
from os import path
#from camera import *
# Initialize the game engine
pygame.init()
# Set the height and width of the screen
size = (WIDTH, HEIGHT) # need a whole number of squares
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tower defense') #set the caption of the game window
#set the icon of the game window
icon = pygame.image.load('minionicon.jpg')
pygame.display.set_icon(icon)
#create fonts
outfit = pygame.font.SysFont('Outfit-Bold.ttf', 35) #font used for text in scoreboard 
#get the map from the text file
game_folder=path.dirname(__file__)
map_data=[]
with open(path.join(game_folder, 'map.txt'), 'rt')as f:
    for line in f:
        map_data.append(line)       
pygame.key.set_repeat(500,100)  #lets held down key repeat
#make the background and set the camera on the center
background = Background("gamebackground.jpg", [0,0])
camera=Camera(1,1)
#########make wall data##############
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
#create the user's pointer
pointer = Pointer(RED, 20, 20)
all_sprites_list.add(pointer) 
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
    #draw the Gameover line
    pygame.draw.line(screen, RED, (50,0), (50, 700))
    #draw the menu bar at the top
    pygame.draw.rect(screen, PURPLE, [0,0, 1000, 100] )
    #draw the scoreboards and the title
    score_board = outfit.render("SCORE: " +  str(score),  True, GREEN)
    Timer = outfit.render("TIME " +  str(timermin ) + ":" + str(timersec),  True, GREEN)
    #highscore_board = outfit.render("HIGHSCORE: " + str(6 * 12 * 20),  True, BLUE)
    screen.blit(score_board, (855, 60))
    screen.blit(Timer, (855, 40))
    all_sprites_list.update()
    for sprite in all_sprites_list:
        screen.blit(sprite.image, camera.apply(sprite))
    #Track the mouse to the pointer
    pos = pygame.mouse.get_pos()
    pointer.rect.x = pos[0]
    pointer.rect.y= pos[1]
    #Make the enemie and bullet move
    for enemy in enemies_list:
        enemy.move(-0.005)
    for bullet in bullets_list:
        bullet.move(0.01)
    #Make the bullets and the enemies kill on collision
    for bullet in bullets_list:
        enemies_hit_list = pygame.sprite.spritecollide(bullet, enemies_list, True)
        if len(enemies_hit_list) > 0:
            bullet.kill()
    #Make the bullets shoot on timer
    bullettimer += 1
    if bullettimer == 180:
        bullettimer = 0
        for plant in plant_list:
            plant.shoot()
    #Check Gameover 
    for enemy in enemies_list:
        gameovercheck = enemy.gameover()
        if gameovercheck == True:
            done = True
    #Timer on the scoreboard
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