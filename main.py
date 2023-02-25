import pygame
import sys
import gamestates.game
import gamestates.menu
import gamestates.choosechar


#create a pygame window

def main(gamestate: str):
    #create a pygame instance and a variable for it
    game = pygame.init()
    pygame.display.set_caption('Pseudocode: The Game')
    #1200 x 800
    screen = pygame.display.set_mode((1200, 800))
    char1: str = ''
    char2: str = ''

    def check_gamestate(gamestate: str, char1: str, char2: str):
        match gamestate:
            case 'menu':
                gamestate = gamestates.menu.main(game, screen)
                check_gamestate(gamestate, char1, char2)
            case 'game':
                gamestate = gamestates.game.main(game, screen, char1, char2)
                check_gamestate(gamestate, char1, char2)
            case 'choosechar':
                [gamestate, char1, char2] = gamestates.choosechar.main(game, screen)
                check_gamestate(gamestate, char1, char2)

    check_gamestate(gamestate, char1, char2)


if __name__ == '__main__':
    gamestate:str = 'menu'
    main('menu') #this is the main module, as described in the structure chart.
