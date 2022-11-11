from Game import Game
from Menus import Menu, Gameoverscreen, OptionsMenu

menu = Menu()
outcome = menu.run()
while outcome != 0:
    if outcome == 1:
        game = Game()
        outcome = game.run()
    elif outcome == 2:
        optionsmenu = OptionsMenu() 
        outcome = optionsmenu.run()
    elif outcome == 3:
        gameoverscreen =  Gameoverscreen()
        outcome = gameoverscreen.run()
    elif outcome == 4:
        menu = Menu()
        outcome = menu.run
    
