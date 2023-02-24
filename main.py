import pygame
import sys
import gamestates.game
import gamestates.menu


#create a pygame window

def main(gamestate: str):
    #create a pygame instance and a variable for it
    game = pygame.init()
    pygame.display.set_caption('Game')
    screen = pygame.display.set_mode(pygame.display.list_modes()[0])


    #switch statement for gamestate
    match gamestate:
        case 'menu':
            gamestates.menu.main(game, screen)
        case 'game':
            gamestates.game.main(game, screen)


if __name__ == '__main__':
    gamestate:str = 'menu'
    main('menu') #this is the main module, as described in the structure chart.
