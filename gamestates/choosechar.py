import pygame
import sys

def main(game, screen):
    chars: str = ['bongleshnout', 'foundlemoup', 'dingledoo', 'maxted']
    render_chars = []

    char1: str = ''
    char2: str = ''

    current_player: int = 1

    for char in chars:
        char = pygame.image.load('assets/' + char + '.png').convert()
        char = pygame.transform.scale(char, (char.get_width() / 3 , char.get_height() / 3))
        render_chars.append(char)

    outline = pygame.image.load('assets/outline.png').convert()
    outline = pygame.transform.scale(outline, (outline.get_width() / 2.8, outline.get_height() / 2.8))

    def draw_chars(iOutline: int = -1):
        for i in range(len(render_chars)):
            if i == iOutline:
                screen.blit(outline, (-130 + render_chars[i].get_width() / 2 + (i * 300), screen.get_height() / 2 - render_chars[i].get_height() / 2 + 100))
            screen.blit(render_chars[i], (-130 + render_chars[i].get_width() / 2 + (i * 300), screen.get_height() / 2 - render_chars[i].get_height() / 2 + 100))


    def clear_draw(player: int, iOutline: int = -1):
        #clear the screen
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('Comic Sans MS', 50)
        text = font.render('Player ' + str(player) + ': Choose your Character!', True, (255, 255, 255))
        #blit the text on the center of the screen
        screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() / 2 - text.get_height() / 2 - 300))
        draw_chars(iOutline)

    clear_draw(current_player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in range(len(render_chars)):
                        if render_chars[i].get_rect(topleft=(-130 + render_chars[i].get_width() / 2 + (i * 300), screen.get_height() / 2 - render_chars[i].get_height() / 2 + 100)).collidepoint(event.pos):
                            if current_player == 1:
                                char1 = chars[i]
                                current_player = 2
                                clear_draw(current_player, i)
                            else:
                                char2 = chars[i]
                                return 'game', char1, char2
                            
            if event.type == pygame.MOUSEMOTION:
                for i in range(len(render_chars)):
                    if render_chars[i].get_rect(topleft=(-130 + render_chars[i].get_width() / 2 + (i * 300), screen.get_height() / 2 - render_chars[i].get_height() / 2 + 100)).collidepoint(event.pos):
                        clear_draw(current_player, i)
                    else:
                        continue

        pygame.display.update()
