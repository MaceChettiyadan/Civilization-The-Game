import pygame
import sys

def main(game, screen):
    while True:
        screen.fill((0, 0, 0))
        #A BOX IN THE MIDDLE OF THE SCREEN, with a white OUTLINE
        pygame.draw.rect(screen, (255, 255, 255), (300, 200, 600, 400), 5)

        #draw the text
        font = pygame.font.SysFont('Monospace', 50)
        text = font.render('About', True, (255, 255, 255))
        screen.blit(text, (400, 250))

        #DESCRIPTION
        font = pygame.font.SysFont('Monospace', 20)
        text = "This game is fully original, \n except the art for the tiles. \n The art is open source, \n made by CuddlyColin on itch.io: \n https://cuddlyclover.itch.io/fantasy-hex-tiles"

        #render text, and split it into lines
        for i, line in enumerate(text.splitlines()):
            screen.blit(font.render(line, True, (255, 255, 255)), (320, 350 + i*20))

        #return to menu button
        pygame.draw.rect(screen, (255, 255, 255), (550, 550, 100, 50))
        font = pygame.font.SysFont('Monospace', 30)
        text = font.render('Menu', True, (0, 0, 0))
        screen.blit(text, (570, 550))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] >= 550 and event.pos[0] <= 650 and event.pos[1] >= 550 and event.pos[1] <= 600: #within bounding box
                return 'menu' #return to menu.py
                        

        pygame.display.update()