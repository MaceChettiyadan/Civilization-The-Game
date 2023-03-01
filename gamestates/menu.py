from math import *
import pygame
import sys


def main(game, screen):
    def draw_UI(play_hover: bool, settings_hover: bool):
        #draw hexagon
        draw_regular_polygon(screen, (249, 224, 118), 6, 80, (550, 350), outlines=True, outline_color=((255, 255, 255) if not play_hover else (250,128,114)), outline_width=4)
        #play text
        font = pygame.font.SysFont('Monospace', 35)
        text = font.render('Play', True, (0, 0, 0))
        screen.blit(text, (510, 330))
        #draw another hexagon bottom right of the first
        draw_regular_polygon(screen, (249, 224, 118), 6, 80, (680, 430), outlines=True, outline_color=((255, 255, 255) if not settings_hover else (250,128,114)), outline_width=4)
        #settings text
        text = font.render('Help', True, (0, 0, 0))
        screen.blit(text, (640, 410))
        #draw text
        font = pygame.font.SysFont('Arial', 50)
        text = font.render('Civilization: The Game', True, (0, 0, 0))

    def draw_regular_polygon(surface, color, vertex_count, radius, position, width=0, outlines=False, outline_color=(0, 0, 0), outline_width=1):
        n, r = vertex_count, radius
        x, y = position
        pygame.draw.polygon(surface, color, [
            (x + r * cos(2 * pi * i / n), y + r * sin(2 * pi * i / n))
            for i in range(n)
        ], width)
        if outlines:
            pygame.draw.polygon(surface, outline_color, [
                (x + r * cos(2 * pi * i / n), y + r * sin(2 * pi * i / n))
                for i in range(n)
            ], outline_width)

    play_hover, settings_hover = False, False

    while True:
        screen.fill((135, 206, 235))
        draw_UI(play_hover, settings_hover)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                #check if mouse is over play button exactly using pythagoras
                if sqrt((event.pos[0] - 550) ** 2 + (event.pos[1] - 350) ** 2) <= 80 and not settings_hover:
                    play_hover = True
                else:
                    play_hover = False
                #check if mouse is over settings button exactly using pythagoras
                if sqrt((event.pos[0] - 670) ** 2 + (event.pos[1] - 420) ** 2) <= 80 and not play_hover:
                    settings_hover = True
                else:
                    settings_hover = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and play_hover:
                    return 'initialise_empire'

        pygame.display.update()