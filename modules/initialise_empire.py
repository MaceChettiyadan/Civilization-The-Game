import pygame
import sys

def main(game, screen):
    def draw_UI(empire_name: str, empire_location: str):
        #draw a rectangle of size 600 x 450 at center of screen
        pygame.draw.rect(screen, (249, 224, 118), (300, 175, 600, 450))
        # draw a 2px border around the rectangle
        pygame.draw.rect(screen, (255, 255, 255), (300, 175, 600, 450), 2)
        # draw text for empire
        font = pygame.font.SysFont('Monospace', 30)
        text = font.render('Name your empire:', True, (0, 0, 0))
        screen.blit(text, (350, 200))
        # draw input box for empire
        pygame.draw.rect(screen, ((255, 255, 255) if not focused_on_name_input else (211,211,211)), (350, 250, 500, 50))
        # draw text for empire
        text = font.render(empire_name, True, (0, 0, 0))
        screen.blit(text, (360, 260))

        # begin button at bottom right of rectangle
        pygame.draw.rect(screen, (249, 224, 118), (650, 550, 200, 50))
        # draw a 2px border around the rectangle
        pygame.draw.rect(screen, ((255, 255, 255) if not begin_hover else (250,128,114)), (650, 550, 200, 50), 2)
        # draw text for begin
        font = pygame.font.SysFont('Monospace', 25)
        text = font.render('Begin', True, (0, 0, 0))
        screen.blit(text, (705, 560))
        text = font.render('Starting Location:', True, (0, 0, 0))
        screen.blit(text, (350, 350))
        dropdown(650, 337, empire_location)

    def dropdown(x: int, y: int, current_option: str):
        #draw rect at x, y
        pygame.draw.rect(screen, (255, 255, 255) if not focused_on_dropdown else (211,211,211), (x, y, 200, 50))
        # add up and down arrows on the right
        pygame.draw.polygon(screen, (0, 0, 0), ((x + 185, y+1), (x + 175, y + 15), (x + 195, y + 15)))
        pygame.draw.polygon(screen, (0, 0, 0), ((x + 185, y + 45), (x + 175, y + 30), (x + 195, y + 30)))
        # draw text for current option
        font = pygame.font.SysFont('Monospace', 25)
        text = font.render(current_option, True, (0, 0, 0))
        screen.blit(text, (x + 10, y + 10))

    empire_name: str = "" #default name
    empire_location: str = "Plains" #default location
    locations: list = ['Mountains', 'Forests', 'Plains', 'Deserts'] #list of locations

    #init booleans
    begin_hover = False
    focused_on_name_input = False
    focused_on_dropdown = False

    while True:
        screen.fill((135, 206, 235)) #fill screen with sky blue
        draw_UI(empire_name, empire_location) #draw UI
        for event in pygame.event.get(): #event loop
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and focused_on_name_input: #if typing in name input
                if event.key == pygame.K_BACKSPACE and len(empire_name) > 0: #if backspace and name is not empty
                    empire_name = empire_name[:-1] #remove last character
                elif len(empire_name) < 26: #if name is less than 26 characters
                    empire_name += event.unicode #add character to name

            if event.type == pygame.MOUSEMOTION: #check if hovering over dropdown
                #check if hovering over begin button
                if 650 < event.pos[0] < 850 and 550 < event.pos[1] < 600:  # if mouse is over begin button
                    begin_hover = True #set bool
                else:
                    begin_hover = False

            if event.type == pygame.MOUSEBUTTONDOWN: #check if clicked on dropdown

                #check if clicked on name input rect
                if 350 < event.pos[0] < 850 and 250 < event.pos[1] < 300:  # if mouse is over name input
                    focused_on_name_input = True
                else:
                    focused_on_name_input = False

                if 825 < event.pos[0] < 855 and 310 < event.pos[1] < 355: # up arrow
                    focused_on_dropdown = True #we set the bool
                    empire_location = locations[locations.index(empire_location) - 1 if locations.index(empire_location) - 1 > -1 else -1] # if index is -1, return last item in list
                elif 825 < event.pos[0] < 855 and 360 < event.pos[1] < 400: # down arrow
                    focused_on_dropdown = True 
                    # if index is len(locations), return first item in list (below)
                    empire_location = locations[locations.index(empire_location) + 1 if locations.index(empire_location) + 1 < len(locations) else 0] 
                elif 650 < event.pos[0] < 850 and 337 < event.pos[1] < 387: # dropdown
                    focused_on_dropdown =True
                else: #none of these, not focused
                    focused_on_dropdown = False

                if begin_hover and len(empire_name) > 0: #if begin button is hovered over and empire name is not empty
                    return 'game', empire_name, empire_location #return game screen
                if len(empire_name) < 1 and begin_hover: #if begin button is hovered over and empire name is empty
                    focused_on_name_input = True #focus on name input
                
        pygame.display.update()
        