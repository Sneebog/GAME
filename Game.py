import pygame
from classes.backgroundclass import Background
from classes.bulletsclass import  Bullets
from classes.cameraclass import Camera
from  classes.enemyclass import Enemies
from  classes.plantclass import Plants
from  classes.pointerclass import Pointer
from newwavespawner import spawnnewwave
import random
#all the classes imported
from variables import *
from os import path
#from camera import *
spawnnum =0 
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
pygame.key.set_repeat(500,100)  #lets held down key repeat
#make the background and set the camera on the center
background = Background("gamebackground.jpg", [0,0])
camera=Camera(1,1)
#create the user's pointer
pointer = Pointer(RED, 20, 20)
all_sprites_list.add(pointer) 
done = False
click = False
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)
# Loop as long as done == False
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loo  
        elif event.type == pygame.mouse.get_pressed:
            click = True
    mouse_buttons = pygame.mouse.get_pressed()
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
    pointer.rect.center = pygame.mouse.get_pos()
    #Make a new plant based on the location
    if mouse_buttons[0] == True:
        pointer.createPlant(pos[0], pos[1],TILESIZE)
    #spawn new enemies
    if timerfps % 12 == 0: 
        spawnnewwave(timerfps)
    #Make the bullets and the enemies kill on collision
    # for bullet in bullets_list:
    #     enemies_hit_list = pygame.sprite.spritecollide(bullet, enemies_list, True)
    #     if enemies_hit_list:   
    #         bullet.kill()
    # if bullet.x > 10: #so that the bullets can't kill enemies spawning in
    #         bullet.kill()
    pygame.sprite.groupcollide(enemies_list, bullets_list, True,True)
    for bullet in bullets_list:
        if bullet.x > 10: 
            bullet.kill
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
    #test bullet kill function
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