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
        text = font.render('Choose your location:', True, (0, 0, 0))
        screen.blit(text, (350, 350))
        dropdown(675, 337, empire_location)

    def dropdown(x: int, y: int, current_option: str):
        #draw rect at x, y
        pygame.draw.rect(screen, (255, 255, 255), (x, y, 200, 50))
        # add up and down arrows on the right
        pygame.draw.polygon(screen, (0, 0, 0), ((x + 185, y), (x + 175, y + 15), (x + 195, y + 15)))
        pygame.draw.polygon(screen, (0, 0, 0), ((x + 185, y + 45), (x + 175, y + 30), (x + 195, y + 30)))
        # draw text for current option
        font = pygame.font.SysFont('Monospace', 25)
        text = font.render(current_option, True, (0, 0, 0))
        screen.blit(text, (x + 10, y + 10))

    empire_name: str = ""
    empire_location: str = "Plains"
    locations: list = ['Mountains', 'Forests', 'Plains']

    begin_hover = False
    focused_on_name_input = False

    while True:
        screen.fill((135, 206, 235))
        draw_UI(empire_name, empire_location)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and focused_on_name_input:
                if event.key == pygame.K_BACKSPACE and len(empire_name) > 0:
                    empire_name = empire_name[:-1]
                elif len(empire_name) < 20:
                    empire_name += event.unicode

            if event.type == pygame.MOUSEMOTION:
                #check if hovering over begin button
                if 650 < event.pos[0] < 850 and 550 < event.pos[1] < 600:
                    begin_hover = True
                else:
                    begin_hover = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                #check if clicked on name input rect
                if 350 < event.pos[0] < 850 and 250 < event.pos[1] < 300:
                    focused_on_name_input = True
                else:
                    focused_on_name_input = False

                if 850 < event.pos[0] < 880 and 310 < event.pos[1] < 355:
                    empire_location = locations[locations.index(empire_location) - 1 if locations.index(empire_location) - 1 > -1 else -1]
                
                if 850 < event.pos[0] < 880 and 360 < event.pos[1] < 400:
                    empire_location = locations[locations.index(empire_location) + 1 if locations.index(empire_location) + 1 < len(locations) else 0]

                if begin_hover and len(empire_name) > 0:
                    return 'game', empire_name, empire_location
                if len(empire_name) < 1 and begin_hover:
                    focused_on_name_input = True
                
        pygame.display.update()
        