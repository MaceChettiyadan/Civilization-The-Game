import pygame
import sys

def main(game, screen, char1: str, char2: str):
    screen.fill((0, 0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
    return 'menu'