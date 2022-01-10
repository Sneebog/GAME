import pygame
from os import path
#from camera import *
 
# Initialize the game engine
pygame.init()
 
# Define some colors
WHITE = (255, 255, 255)
BLACK= (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
#TILES
WIDTH=1000
HEIGHT=700
TILESIZE=100
GRIDWIDTH = WIDTH/TILESIZE  #  10 squares
GRIDHEIGHT = HEIGHT/TILESIZE # 7 squares
#funny variables
chimbus = 0
score = 0 
timerfps= 0
timer = 120
timersec = 0
timermin = 0
# Set the height and width of the screen
size = (WIDTH, HEIGHT) # need a whole number of squares so wholly divisible by 32
screen = pygame.display.set_mode(size)

game_folder=path.dirname(__file__)
map_data=[]
with open(path.join(game_folder, 'map.txt'), 'rt')as f:
    for line in f:
        map_data.append(line)       
pygame.key.set_repeat(500,100)  #lets held down key repeat


######## classes  ############
class Pointer(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
class entity(pygame.sprite.Sprite):
    def __init__(self, x, y, TILESIZE):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(WHITE)
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
    def update(self):
        self.rect.x=self.x*TILESIZE   #multiply the x and y by tilesize to draw on screen
        self.rect.y=self.y*TILESIZE
class enemies(entity):
    def __init__(self, x, y , tilesize):
        super().__init__(x,y, tilesize)
        self.image.fill(RED)
    def update(self):
        super().update()
    def move(self, x_offset):
        self.x += x_offset       
class plants(entity):
    def __init__(self, x, y , tilesize):
        super().__init__(x,y, tilesize)
        self.image.fill(RED)
    def update(self):
        super().update()
    def shoot(self):
        bullet = bullets(self.x, self.y, 5, 5)  
        all_sprites_list.add(bullet)
        bullets_list.add(bullet)
class bullets(entity):
    def __init__(self, x, y , width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.width = width
        self.height = height
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
    def update(self):
        self.rect.x=self.x*TILESIZE  #multiply the x and y by tilesize to draw on screen
        self.rect.y=(self.y*TILESIZE) + 50
    def move(self, x_offset):
        self.x += x_offset
class Camera:
    def __init__(self, width, height):
        self.camera=pygame.Rect(0,0, width, height)
        self.width=width
        self.height=height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH/2)
        y = -target.rect.y + int(HEIGHT/2)
        x=min(0,x) #stops going off on left
        y=min(0,y) #stops going off on top
       # x=max(-1024-2080,x)
        x=max(-(2080-1024),x)
        y=max(-(800-HEIGHT),y)
        
        self.camera = pygame.Rect(x, y, self.width, self.height)
class Background(pygame.sprite.Sprite):
        def __init__(self, image_file, location):
            pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
            self.image = pygame.image.load(image_file)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location
Background = Background("game background.jpg", [0,0])
camera=Camera(1,1)


########make groups########

all_sprites_list = pygame.sprite.Group() #group for all objects
enemies_hit_list = pygame.sprite.Group()
enemies_list = pygame.sprite.Group()
plant_list = []
bullets_list = pygame.sprite.Group()
#create fonts
outfit = pygame.font.SysFont('Outfit-Bold.ttf', 35)
#########make wall data##############
pointer = Pointer(RED, 20, 20)
all_sprites_list.add(pointer)
for row, tiles in enumerate(map_data):  #enumerate returns the index value of the item
    for col, tile in enumerate(tiles):  #enumerate returns the index value of the item
        if tile=="1":
            enemy=enemies(col, row, TILESIZE)  #col will be the number of the column, row the number enumerated when the 1 is found
            all_sprites_list.add(enemy)
            enemies_list.add(enemy) #add wall to wall group
        if tile == "2":
            plant = plants(col, row, TILESIZE)
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
    screen.blit(Background.image, Background.rect)
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