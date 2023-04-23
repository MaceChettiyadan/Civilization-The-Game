import pygame
import sys

def main(game, screen, reason_over):
    while True:
        screen.fill((0, 0, 0))
        #A BOX IN THE MIDDLE OF THE SCREEN, with a white OUTLINE
        pygame.draw.rect(screen, (255, 255, 255), (300, 200, 600, 400), 5)

        #draw the text
        font = pygame.font.SysFont('Monospace', 50)
        text = font.render('Game Over', True, (255, 255, 255))
        screen.blit(text, (400, 250))
        #draw the reason for game over
        font = pygame.font.SysFont('Monospace', 20)
        text = font.render("Over by " + reason_over, True, (255, 255, 255))
        screen.blit(text, (400, 350))

        #draw the button
        pygame.draw.rect(screen, (255, 255, 255), (550, 400, 100, 50))
        font = pygame.font.SysFont('Monospace', 30)
        text = font.render('Menu', True, (0, 0, 0))
        screen.blit(text, (570, 410))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = event.pos
                    if mouse_pos[0] >= 550 and mouse_pos[0] <= 650:
                        if mouse_pos[1] >= 400 and mouse_pos[1] <= 450:
                            return 'menu'
                        
        pygame.display.update()