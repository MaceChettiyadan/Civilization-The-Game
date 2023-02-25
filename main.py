import pygame
import sys
import gamestates.game
import gamestates.menu


#create a pygame window

def main(gamestate: str):
    #create a pygame instance and a variable for it
    game = pygame.init()
    pygame.display.set_caption('Pseudocode: The Game')
    screen = pygame.display.set_mode(pygame.display.list_modes()[0])

    def check_gamestate(gamestate: str):
        match gamestate:
            case 'menu':
                gamestate = gamestates.menu.main(game, screen)
                check_gamestate(gamestate)
            case 'game':
                gamestate = gamestates.game.main(game, screen)
                check_gamestate(gamestate)

    check_gamestate(gamestate)


if __name__ == '__main__':
    gamestate:str = 'menu'
    main('menu') #this is the main module, as described in the structure chart.
