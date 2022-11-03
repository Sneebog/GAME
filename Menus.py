import pygame
from classes.backgroundclass import Background 
from variables import *
class Menu():
    def __init__(self):
        #set the size of the screen
        self.size = (600, 800)
        self.background = Background("menubackground.jpg", [0,0])
        self.done = False
        #allow game to finish

    def run(self):
        # Initialize the game engine
        pygame.init()
        #set the screen etc
        screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Tower Defense Main Menu') #set the caption of the game window
        clock = pygame.time.Clock()
        pygame.key.set_repeat(500,100)  #lets held down key repeat
        while not self.done:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    self.done = True  # Flag that we are done so we exit this loo  
                elif event.type == pygame.mouse.get_pressed():
                    click = True 
                screen.fill(WHITE)
                #set the background image
                screen.blit(self.background.image, self.background.rect)
                pygame.display.flip()
            # Check the list of collisions


            clock.tick(60)
        # Be IDLE friendly
        pygame.quit()
menu = Menu()
menu.run()