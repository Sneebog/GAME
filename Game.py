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
class Game():
    def __init__(self):
        # Set the height and width of the screen
        self.size = (WIDTH, HEIGHT) #need a whole number of squares
        #make the background and set the camera on the center
        self.background = Background("gamebackground.jpg", [0,0])
        self.score = 0
        self.sun = 0
        self.currency = 100
        self.timer = 0
        self.timersec = 0
        self.timermin = 0
        self.bullettimer = 0
        self.wavenum = 1
        self.timerfps = 0
        self.outcome = 0
        self.clicktemp = 0
        self.finalbarrier = True #game final barrier
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
        pointer_list.add(pointer)
        clock = pygame.time.Clock()
        pygame.mouse.set_visible(False)
        
        # Loop as long as done == False
        sClick = False

        #create the shop images
        plantshop = Background("Peashootershopicon.png", [100, 0])
        sunflowershop = Background("flowershopicon.png", [200, 0])
        
        #towerdefense logo
        tdlogo = Background("towerdefenselogo.jpg", [315, 0])


        while not self.done:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    self.done = True  # Flag that we are done so we exit this loop

                   
                # checking if keydown event happened or not
                if event.type == pygame.KEYDOWN:
               
                    if event.key == pygame.K_s:
                        sClick =  True

            mouse_buttons = pygame.mouse.get_pressed()
            screen.fill(WHITE)

            #set the background image
            screen.blit(self.background.image, self.background.rect)

            #create the lines to partition the screen
            for x in range(0, WIDTH, TILESIZE):
                pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT)) #draws vertical lines every TILESIZE and going as far as HEIGHT down
            for y in range(0, HEIGHT, TILESIZE):
                pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y)) #draws horizontal lines every TILESIZE and going across as far as WIDTH
            
            #draw the Gameover line
            pygame.draw.line(screen, RED, (50,0), (50, 700))
            #draw the menu bar at the top
            pygame.draw.rect(screen, PURPLE, [0,0, 1000, 100] )

            #set the shop images
            screen.blit(plantshop.image, plantshop.rect)
            screen.blit(sunflowershop.image, sunflowershop.rect)
            #draw the shop text
            shoptext = outfit.render("Shop: ",  True, RED)
            costtext = outfit.render("Cost: ",  True, RED)
            screen.blit(shoptext, (20, 10))
            screen.blit(costtext, (20, 70))
            #draw text for shop prices
            plantprice = outfit.render("20 ",  True, RED)
            flowerprice = outfit.render("15 ",  True, RED)
            screen.blit(plantprice, (140, 70))
            screen.blit(flowerprice, (240, 70))

            #draw td logo
            screen.blit(tdlogo.image, tdlogo.rect)

            #draw the scoreboards and the title
            score_board = outfit.render("SCORE: " +  str(self.score),  True, GREEN)
            Timer = outfit.render("TIME " +  str(self.timermin ) + ":" + str(self.timersec),  True, GREEN)
            screen.blit(score_board, (855, 60))
            screen.blit(Timer, (855, 40))

            #currency on the screen
            currency_board = outfit.render("Flower Power: " +  str(self.currency),  True, GREEN)
            screen.blit(currency_board, (600, 60))

            #Final barrier
            finalbarrier = outfit.render("Finalbarrier: " + str(self.finalbarrier), True, GREEN)
            screen.blit(finalbarrier, (600, 40))

            #draw sprites
            all_sprites_list.update()
            all_sprites_list.draw(screen)
            #make the pointer on the front of the screen
            pointer_list.draw(screen)
            #Track the mouse to the pointer
            pos = pygame.mouse.get_pos()
            pointer.rect.center = pygame.mouse.get_pos()
            #Make a new plant based on the location
            if mouse_buttons[0] == True:
                if self.clicktemp > 10:
                    self.currency = pointer.createPlant(pos[0], pos[1],TILESIZE, "peashooter", self.currency )
                    self.clicktemp = 0
                else:
                    self.clicktemp += 1
            #make a new sunflower based on the location
            elif sClick == True:
                self.currency = pointer.createPlant(pos[0], pos[1],TILESIZE, "sunflower", self.currency)
            #spawn new enemies
            if self.timerfps % 12 == 0: 
                spawnnewwave(self.timerfps)
            #enemy checks 
            for enemy in enemies_list:
                #Make the bullets and the enemies kill on collision
                if pygame.sprite.spritecollide(enemy,bullets_list,True): #kills the bullets
                    temp = self.score
                    self.score = enemy.damage(self.score) #damages the enemy and also calculates the score for the scoreboard
                    if self.score > temp:
                        self.currency += 20
                for plant in plant_list:
                    heldplant.add(plant)
                    if pygame.sprite.spritecollide(enemy, heldplant, False):
                        plant.damage()
                #make the enemies damage the plants
                #Gameover check for the enemies
                gameovercheck = enemy.gameover()
                if gameovercheck == True:
                    if self.finalbarrier == True:  #check if final barrier is active
                        enemy.kill()
                        self.finalbarrier = False #if activated remove the final barrier 
                    else:
                        self.finalbarrier = True
                        self.done = True
                        self.outcome = 3
            
            #make the sunbullets increase the currency
            if pygame.sprite.spritecollide(pointer, sunbullets_list, True): #kills sun bullets
                self.currency += 5
            #check the score 
            if self.score == 100:
                self.done = True
           
            # #Make the bullets shoot on timer
            for plant in plant_list:
                if plant.timer == 180:
                    plant.shoot()


            for sun in sunbullets_list:
                if sun.timer >= 240:
                    sun.kill()


            #Timer on the scoreboard
            self.timerfps += 1
            if self.timerfps == 60:
                self.timerfps = 0 
                self.timer += 1
                self.timermin = self.timer // 60
                self.timersec = self.timer % 60
            
            sClick = False
            pygame.display.flip()

            clock.tick(60)
        # Be IDLE friendly
        pygame.quit()
        #delete all the sprites
        all_sprites_list.empty()
        pointer_list.empty()

        return self.outcome
