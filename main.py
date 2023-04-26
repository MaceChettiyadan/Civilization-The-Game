#essential modules
import pygame
import sys

#these are my own modules
import modules.game
import modules.menu
import modules.initialise_empire
import modules.game_over
import modules.about

#create a pygame window

def main(gamestate: str):
    #create a pygame instance and a variable for it
    game = pygame.init()
    pygame.display.set_caption('Civilization: The Game')
    #1200 x 800
    screen = pygame.display.set_mode((1200, 800)) #create a pygame window

    empire_name: str = "" #default name
    empire_location: str = "" #default location

    def slideInOut():
        x = 0
        while True:
            delta_time = pygame.time.Clock().tick(60) / 1000 #get delta time
            x += delta_time * 6000
            #slide in a rect from the left
            screen.fill((0, 0, 0))
            # slide in rect from left ease in out   
            pygame.draw.rect(screen, (249, 224, 118), (x, 0, 1200, 267))
            pygame.draw.rect(screen, (209, 224, 118), (x*1.05, 267, 1200, 267)) 
            pygame.draw.rect(screen, (189, 224, 118), (x*1.1, 534, 1200, 267)) #increase x ease in out

            # increase x ease in out
            if x >= 1200:
                return
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update() #update the display


    def check_gamestate(gamestate: str, empire_name: str, empire_location: str, reason_over: str = None):
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        match gamestate:
            case 'menu': #if gamestate is menu
                slideInOut() #slide in the menu
                gamestate = modules.menu.main(game, screen) #run the menu module
                check_gamestate(gamestate, empire_name, empire_location) #check the gamestate
            case 'game':
                slideInOut() #slide in the game
                gamestate, reason_over = modules.game.main(game, screen, empire_name, empire_location) #run the game module
                check_gamestate(gamestate, empire_name, empire_location, reason_over) #check the gamestate
            case 'initialise_empire':
                slideInOut() #slide in the initialise empire
                gamestate, empire_name, empire_location = modules.initialise_empire.main(game, screen) #run the initialise empire module
                check_gamestate(gamestate, empire_name, empire_location) #check the gamestate
            case 'game_over':
                slideInOut() #slide in the game over
                gamestate = modules.game_over.main(game, screen, reason_over) #run the game over module
                check_gamestate(gamestate, empire_name, empire_location) #check the gamestate
            case 'about':
                slideInOut() #slide in the about
                gamestate = modules.about.main(game, screen)
                check_gamestate(gamestate, empire_name, empire_location) #check the gamestate

    check_gamestate(gamestate, empire_name, empire_location, "") 





if __name__ == '__main__':
    gamestate:str = 'menu'
    main('menu') #this is the main module, as described in the structure chart.