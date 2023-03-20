from Game import Game
from Menus import Menu, Gameoverscreen, OptionsMenu

menu = Menu() # opens the Menu for the first time
outcome = menu.run() 

while outcome != 0: #constantly runs till user closes it 
    if outcome == 1:
        game = Game() #opens the main game
        outcome = game.run()  
    elif outcome == 2:
        optionsmenu = OptionsMenu() #opens the options menu
        outcome = optionsmenu.run()
    elif outcome == 3:
        gameoverscreen =  Gameoverscreen() #opens the gameover screen
        outcome = gameoverscreen.run()
    elif outcome == 4:
        menu = Menu() #opens the menu 
        outcome = menu.run()