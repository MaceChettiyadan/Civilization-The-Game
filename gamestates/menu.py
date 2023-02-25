import pygame
import sys


def main(game, screen):
    def draw_button(path: str, scale: float):
        button = pygame.image.load(path).convert()
        button = pygame.transform.scale(button, (button.get_width() / scale, button.get_height() / scale))
        screen.blit(button, (screen.get_width() / 2 - button.get_width() / 2, screen.get_height() / 2 - button.get_height() / 2))
        return button
    
    def clear_draw():
        #clear the screen
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('Comic Sans MS', 60)
        text = font.render('Pseudocode: The Game', True, (255, 255, 255))
        #blit the text on the center of the screen
        screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() / 2 - text.get_height() / 2 - 300))

    clear_draw()
    play_button = draw_button('assets/playbutton.png', 1.5)
    isHover: bool = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if play_button.get_rect(topleft=(screen.get_width() / 2 - play_button.get_width() / 2, screen.get_height() / 2 - play_button.get_height() / 2)).collidepoint(event.pos):
                        return 'choosechar'
                    
            #CHECK FOR MOUSE OVER THE PLAY BUTTON
            if event.type == pygame.MOUSEMOTION:
                if play_button.get_rect(topleft=(screen.get_width() / 2 - play_button.get_width() / 2, screen.get_height() / 2 - play_button.get_height() / 2)).collidepoint(event.pos):
                    if not isHover:
                        clear_draw()
                        play_button = draw_button('assets/playbutton.png', 1.2)
                    isHover = True
                else:
                    if isHover:
                        clear_draw()
                        play_button = draw_button('assets/playbutton.png', 1.5)
                    isHover = False

        pygame.display.update()