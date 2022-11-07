import pygame
from variables import *
class buttons(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
        self.rect=self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        self.rect.x=self.x
        self.rect.y=self.y

class Textbuttons(buttons):
    def __init__(self, x, y, width, height, Textinput, font):
        super().__init__(x, y, width, height)
        self.textInput = Textinput
        self.font = font
        self.text = self.font.render(self.textInput, True, GREY)

    def update(self):
        super().update()
        #screen.blit(self.text, (self.x, self.y) )
        
    def textdraw(self, screen):
        screen.blit(self.text, (self.x, self.y) )