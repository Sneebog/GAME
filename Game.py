import pygame
from classes.backgroundclass import Background
from classes.bulletsclass import  Bullets
from  classes.enemyclass import Enemies
from  classes.plantclass import Plants
from  classes.pointerclass import Pointer
from newwavespawner import spawnnewwave
import random
#all the classes imported
from variables import *
spawnnum =0 
class Game():
    def __init__(self):
        # Set the height and width of the screen
        self.size = (WIDTH, HEIGHT) #need a whole number of squares
        #make the background and set the camera on the center
        self.background = Background("gamebackground.jpg", [0,0])
        self.score = 0
        self.timer = 120
        self.timersec = 0
        self.timermin = 0
        self.bullettimer = 0
        self.wavenum = 1
        self.timerfps = 0
        #determines when to close the game
        self.done = False
        
    def run(self):
        # Initialize the game engine
        pygame.init()
        #set the screen
        screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Tower defense') #set the caption of the game window
        #set the icon of the game window
        icon = pygame.image.load('minionicon.jpg')
        pygame.display.set_icon(icon)
        #create fonts
        outfit = pygame.font.SysFont('Outfit-Bold.ttf', 35) #font used for text in scoreboard     
        pygame.key.set_repeat(500,100)  #lets held down key repeat
        #create the user's pointer
        pointer = Pointer(RED, 20, 20)
        all_sprites_list.add(pointer) 
        clock = pygame.time.Clock()
        pygame.mouse.set_visible(False)
        # Loop as long as done == False

        while not self.done:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    self.done = True  # Flag that we are done so we exit this loo  
            mouse_buttons = pygame.mouse.get_pressed()
            screen.fill(WHITE)
            #set the background image
            screen.blit(self.background.image, self.background.rect)
            for x in range(0, WIDTH, TILESIZE):
                pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT)) #draws vertical lines every TILESIZE and going as far as HEIGHT down
            for y in range(0, HEIGHT, TILESIZE):
                pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y)) #draws horizontal lines every TILESIZE and going across as far as WIDTH
            #draw the Gameover line
            pygame.draw.line(screen, RED, (50,0), (50, 700))
            #draw the menu bar at the top
            pygame.draw.rect(screen, PURPLE, [0,0, 1000, 100] )
            #draw the scoreboards and the title
            score_board = outfit.render("SCORE: " +  str(self.score),  True, GREEN)
            Timer = outfit.render("TIME " +  str(self.timermin ) + ":" + str(self.timersec),  True, GREEN)
            #highscore_board = outfit.render("HIGHSCORE: " + str(6 * 12 * 20),  True, BLUE)
            screen.blit(score_board, (855, 60))
            screen.blit(Timer, (855, 40))
            all_sprites_list.update()
            all_sprites_list.draw(screen)
            #Track the mouse to the pointer
            pos = pygame.mouse.get_pos()
            pointer.rect.center = pygame.mouse.get_pos()
            #Make a new plant based on the location
            if mouse_buttons[0] == True:
                pointer.createPlant(pos[0], pos[1],TILESIZE)
            #spawn new enemies
            if self.timerfps % 12 == 0: 
                spawnnewwave(self.timerfps)
            #enemy checks 
            for enemy in enemies_list:
                #Make the bullets and the enemies kill on collision
                if pygame.sprite.spritecollide(enemy,bullets_list,True): #kills the bullets
                    self.score = enemy.damage(self.score) #damages the enemy and also calculates the score for the scoreboard
                for plant in plant_list:
                    heldplant.add(plant)
                    if pygame.sprite.spritecollide(enemy, heldplant, False):
                        plant.damage()
                #make the enemies damage the plants
                #Gameover check for the enemies
                gameovercheck = enemy.gameover()
                if gameovercheck == True:
                    self.done = True

                  
           
            # pygame.sprite.groupcollide(enemies_list, bullets_list, False, True)
            # for bullet in bullets_list:
            #     if bullet.x > 10:   #so that the bullets can't kill enemies spawning in
            #         bullet.kill


            #Make the bullets shoot on timer
            self.bullettimer += 1
            if self.bullettimer == 180:
                self.bullettimer = 0
                for plant in plant_list:
                    plant.shoot()

            #Timer on the scoreboard
            self.timerfps += 1
            if self.timerfps == 60:
                self.timerfps = 0 
                self.timer -= 1
                self.timermin = self.timer // 60
                self.timersec = self.timer % 60

            pygame.display.flip()

            clock.tick(60)
        # Be IDLE friendly
        pygame.quit()
game = Game()
game.run()