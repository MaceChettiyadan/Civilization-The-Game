import pygame
import sys
import gamestates.game
import gamestates.menu
import gamestates.initialise_empire

#create a pygame window

def main(gamestate: str):
    #create a pygame instance and a variable for it
    game = pygame.init()
    pygame.display.set_caption('Civilization: The Game')
    #1200 x 800
    screen = pygame.display.set_mode((1200, 800))

    empire_name: str = ""
    empire_location: str = ""

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


    def check_gamestate(gamestate: str, empire_name: str, empire_location: str):
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        match gamestate:
            case 'menu':
                slideInOut()
                gamestate = gamestates.menu.main(game, screen)
                check_gamestate(gamestate, empire_name, empire_location)
            case 'game':
                slideInOut()
                gamestate = gamestates.game.main(game, screen)
                check_gamestate(gamestate, empire_name, empire_location)

            case 'initialise_empire':
                slideInOut()
                gamestate, empire_name, empire_location = gamestates.initialise_empire.main(game, screen)
                check_gamestate(gamestate, empire_name, empire_location)

    check_gamestate(gamestate, empire_name, empire_location)





if __name__ == '__main__':
    gamestate:str = 'menu'
    main('menu') #this is the main module, as described in the structure chart.
