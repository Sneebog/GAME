import pygame
from classes.backgroundclass import Background 
from variables import *
from classes.buttons import buttons, Textbuttons
class Menu():
    def __init__(self):
        #set the size of the screen
        self.size = (600, 800)
        self.background = Background("gravebackground.jpg", [0,0])
        self.done = False
        #allow game to finish
        self.click = False
        #allow for player inputs
        self.outcome = 0
        #To find what is displayed next, e.g. the game runs
        self.menuspriteslist = pygame.sprite.Group() #group for all objects in menu
    def run(self):
        # Initialize the game engine
        pygame.init()
        #set the screen etc
        screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Tower Defense Main Menu') #set the caption of the game window
        #create fonts
        outfit = pygame.font.SysFont('Outfit-Bold.ttf', 35) #font used for text in scoreboard     
        clock = pygame.time.Clock()
        pygame.key.set_repeat(500,100)  #lets held down key repeat
        #create the text blocks
        startbutton = Textbuttons(200, 375, 200, 50, GREY, "Start", outfit, RED)
        optionsbutton = Textbuttons(200, 445, 200, 50,GREY, "Options", outfit, RED )
        quitbutton = Textbuttons(200, 515, 200, 50,GREY, "Quit", outfit, RED )
        self.menuspriteslist.add(startbutton, optionsbutton, quitbutton)
      
        while not self.done:

            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    self.done = True  # Flag that we are done so we exit this loop

            mouse_buttons = pygame.mouse.get_pressed() #get the mouse inputs
            pos = pygame.mouse.get_pos() #get the mouse position
            if mouse_buttons[0] == True: #if left click is clicked set flag click to true
                self.click = True
            
            screen.fill(WHITE)
            #set the background image
            screen.blit(self.background.image, self.background.rect)
            #draw the buttons
            self.menuspriteslist.draw(screen)
            #correct the buttons positions and display any text
            self.menuspriteslist.update(screen)

            #Check if the player has clicked a button
            if self.click == True:
                for button in self.menuspriteslist: #check every button in list
                        button.checkclick(pos[0], pos[1]) #if the mouse is on the buttons position the button will have click set to true
            #check the buttons that are clicked
            if startbutton.click == True:
                self.outcome = 1 #game starts
            elif optionsbutton.click == True:
                self.outcome = 2 #open options menu
            elif quitbutton.click == True:#closes the menu
                self.outcome = 3

            #close the screen
            if self.outcome != 0:
                self.done = True
            
            pygame.display.flip()

            clock.tick(60)
        pygame.quit()
        return self.outcome
        
class OptionsMenu(Menu):
    def __init__(self):
        super().__init__()
        self.background = Background("gamebackground.jpg", [0,0])
    
    def run(self):
        # Initialize the game engine
        pygame.init()
        #set the screen etc
        screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Tower Defense Options Menu') #set the caption of the game window
        #create fonts
        #outfit = pygame.font.SysFont('Outfit-Bold.ttf', 35) #font used for text in scoreboard     
        clock = pygame.time.Clock()
        pygame.key.set_repeat(500,100)  #lets held down key repeat

        while not self.done:

            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    self.done = True  # Flag that we are done so we exit this loop

            mouse_buttons = pygame.mouse.get_pressed() #get the mouse inputs
            pos = pygame.mouse.get_pos() #get the mouse position
            if mouse_buttons[0] == True: #if left click is clicked set flag click to true
                self.click = True
            
            screen.fill(WHITE)
            #set the background image
            #screen.blit(self.background.image, self.background.rect)
    
            pygame.display.flip()

            clock.tick(60)
        pygame.quit()
        return self.outcome

class Gameoverscreen(Menu):
    def __init__(self):
        super().__init__()
        self.size = (1000, 700)
        self.background = Background("gameoverscreen.jpg", [0,0])

    def run(self):
        pygame.init()
        #set the screen etc
        screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Tower Defense Gameover Screen') #set the caption of the game window
        #create fonts
        outfit = pygame.font.SysFont('Outfit-Bold.ttf', 35) #font used for text in scoreboard     
        clock = pygame.time.Clock()
        pygame.key.set_repeat(500,100)  #lets held down key repeat
        replaybutton = Textbuttons(200, 600, 200, 50,ORANGE, "Replay", outfit, WHITE)
        quitbutton = Textbuttons(600, 600, 200, 50,PROPERPURP, "Quit", outfit, WHITE)
        self.menuspriteslist.add(replaybutton, quitbutton)
        while not self.done:

                    for event in pygame.event.get():  # User did something
                        if event.type == pygame.QUIT:  # If user clicked close
                            self.done = True  # Flag that we are done so we exit this loop

                    mouse_buttons = pygame.mouse.get_pressed() #get the mouse inputs
                    pos = pygame.mouse.get_pos() #get the mouse position
                    if mouse_buttons[0] == True: #if left click is clicked set flag click to true
                        self.click = True
                    
                    screen.fill(WHITE)
                    #set the background image
                    screen.blit(self.background.image, self.background.rect)
                    #draw the buttons
                    self.menuspriteslist.draw(screen)
                    #correct the buttons positions and display any text
                    self.menuspriteslist.update(screen)
                    #Check if the player has clicked a button
                    if self.click == True:
                        for button in self.menuspriteslist: #check every button in list
                                button.checkclick(pos[0], pos[1]) #if the mouse is on the buttons position the button will have click set to true
                    #check the buttons that are clicked
                    if replaybutton.click == True:
                        self.outcome = 1 #game starts
                    elif quitbutton.click == True:#closes the game
                        self.outcome = 3

                    #close the screen
                    if self.outcome != 0:
                        self.done = True
                    
                    pygame.display.flip()

                    clock.tick(60)
        pygame.quit()


gameover = Gameoverscreen()
gameover.run()