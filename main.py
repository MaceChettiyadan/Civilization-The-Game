import pygame
import sys
import gamestates.game
import gamestates.menu
import gamestates.choosechar
import gamestates.versus

#create a pygame window

def main(gamestate: str):
    #create a pygame instance and a variable for it
    game = pygame.init()
    pygame.display.set_caption('Pseudocode: The Game')
    #1200 x 800
    screen = pygame.display.set_mode((1200, 800))
    char: str = ''

    def slideInOut():
        x = 0
        while True:
            delta_time = pygame.time.Clock().tick(60) / 1000
            x += delta_time * 6000
            #slide in a rect from the left
            screen.fill((0, 0, 0))
            # slide in rect from left ease in out
            pygame.draw.rect(screen, (249, 224, 118), (x, 0, 1200, 267))
            pygame.draw.rect(screen, (209, 224, 118), (x*1.05, 267, 1200, 267))
            pygame.draw.rect(screen, (189, 224, 118), (x*1.1, 534, 1200, 267))

            # increase x ease in out
            if x >= 1200:
                return
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

    ai = ''

    def check_gamestate(gamestate: str, char: str, ai: str):
        match gamestate:
            case 'menu':
                slideInOut()
                gamestate = gamestates.menu.main(game, screen)
                check_gamestate(gamestate, char, ai)
            case 'game':
                slideInOut()
                gamestate = gamestates.game.main(game, screen, char, ai)
                check_gamestate(gamestate, char, ai)
            case 'choosechar':
                slideInOut()
                [gamestate, char] = gamestates.choosechar.main(game, screen)
                check_gamestate(gamestate, char, ai)
            case 'versus':
                slideInOut()
                [gamestate, ai] = gamestates.versus.main(game, screen, char)
                check_gamestate(gamestate, char, ai)


    check_gamestate(gamestate, char, ai)





if __name__ == '__main__':
    gamestate:str = 'menu'
    main('menu') #this is the main module, as described in the structure chart.
