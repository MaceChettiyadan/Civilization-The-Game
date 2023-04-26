from math import *
import pygame
import sys


def main(game, screen):
    def draw_UI(play_hover: bool, about_hover: bool):
        #draw hexagon
        draw_regular_polygon(screen, (0,0,0), 6, 80, (550, 350), outlines=True, outline_color=((255, 255, 255) if not play_hover else (250,128,114)), outline_width=4)
        #play text
        font = pygame.font.SysFont('Monospace', 35)
        text = font.render('Play', True, (255, 255, 255))
        screen.blit(text, (510, 330))
        #draw another hexagon bottom right of the first
        draw_regular_polygon(screen, (0,0,0), 6, 80, (680, 430), outlines=True, outline_color=((255, 255, 255) if not about_hover else (250,128,114)), outline_width=4)
        #about text
        text = font.render('About', True, (255, 255, 255))
        screen.blit(text, (640, 410))
        #draw text
        font = pygame.font.SysFont('Arial', 50)
        text = font.render('Civilization: The Game', True, (0, 0, 0))

    def draw_regular_polygon(surface, color, vertex_count, radius, position, width=0, outlines=False, outline_color=(0, 0, 0), outline_width=1):
        n, r = vertex_count, radius # n is the number of vertices, r is the radius
        x, y = position # x and y are the coordinates of the center of the polygon
        pygame.draw.polygon(surface, color, [ # draw the polygon
            (x + r * cos(2 * pi * i / n), y + r * sin(2 * pi * i / n))
            for i in range(n)
        ], width)
        if outlines: # draw the outline if outlines is True
            pygame.draw.polygon(surface, outline_color, [ # draw the outline
                (x + r * cos(2 * pi * i / n), y + r * sin(2 * pi * i / n))
                for i in range(n)
            ], outline_width) # draw the outline

    play_hover, about_hover = False, False #initialise variables

    while True:
        screen.fill((0,0,0)) #fill screen with black
        draw_UI(play_hover, about_hover) #draw UI
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION: #check if mouse is over play button
                #check if mouse is over play button exactly using pythagoras
                if sqrt((event.pos[0] - 550) ** 2 + (event.pos[1] - 350) ** 2) <= 80 and not about_hover:
                    play_hover = True
                else:
                    play_hover = False
                #check if mouse is over about button exactly using pythagoras
                if sqrt((event.pos[0] - 670) ** 2 + (event.pos[1] - 420) ** 2) <= 80 and not play_hover:
                    about_hover = True 
                else:
                    about_hover = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and play_hover: #check if left mouse button is pressed and mouse is over play button
                    return 'initialise_empire' #return to initialise_empire.py
                if event.button == 1 and about_hover: #check if left mouse button is pressed and mouse is over about button
                    return 'about' #return to about.py

        pygame.display.update()