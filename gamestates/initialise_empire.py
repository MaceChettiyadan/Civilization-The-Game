import pygame
import sys

def main(game, screen):
    def draw_UI(empire_name: str):
        #draw a rectangle of size 600 x 450 at center of screen
        pygame.draw.rect(screen, (249, 224, 118), (300, 175, 600, 450))
        # draw a 2px border around the rectangle
        pygame.draw.rect(screen, (255, 255, 255), (300, 175, 600, 450), 2)
        # draw text for empire
        font = pygame.font.SysFont('Monospace', 30)
        text = font.render('Name your empire:', True, (0, 0, 0))
        screen.blit(text, (350, 200))
        # draw input box for empire
        pygame.draw.rect(screen, (255, 255, 255), (350, 250, 500, 50))
        # draw text for empire
        text = font.render(empire_name, True, (0, 0, 0))
        screen.blit(text, (360, 260))

        # begin button at bottom right of rectangle
        pygame.draw.rect(screen, (249, 224, 118), (650, 500, 200, 50))
        # draw a 2px border around the rectangle
        pygame.draw.rect(screen, (255, 255, 255), (650, 500, 200, 50), 2)
        # draw text for begin
        font = pygame.font.SysFont('Monospace', 20)
        text = font.render('Begin', True, (0, 0, 0))
        screen.blit(text, (700, 510))

    empire_name: str = ""

    while True:
        screen.fill((135, 206, 235))
        draw_UI(empire_name)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    empire_name = empire_name[:-1]
                else:
                    empire_name += event.unicode
        pygame.display.update()
        