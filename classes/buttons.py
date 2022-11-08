import pygame

class buttons(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.x = x
        self.y = y
        self.click = False #set click flag as false

    def update(self):
        self.rect.x=self.x #draws the block on the screen
        self.rect.y=self.y

    def checkclick(self, mousex, mousey):
        if mousex >= self.x and mousex <= self.x + self.width: #ensure the mouse's x is within the block
            if mousey >= self.y and mousey <= self.y + self.height: #ensure the mouse'y is within the block
                self.click = True


class Textbuttons(buttons):
    def __init__(self, x, y, width, height,color, Textinput, font, textcolour):
        super().__init__(x, y, width, height, color)
        self.textInput = Textinput
        self.font = font
        self.text = self.font.render(self.textInput, True, textcolour) #render the text to be later displayed
        self.xcenter = self.x + ((self.width / 2) - 35) #used to center the buttons
        self.ycenter = self.y + ((self.height / 2) - 15)

    def update(self, screen):
        super().update()
        screen.blit(self.text, (self.xcenter, self.ycenter) ) #draw the text at the blocks position

    def checkclick(self, mousex, mousey):
        super().checkclick(mousex, mousey)