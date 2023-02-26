import pygame
import sys

def main(game, screen):
    chars: str = ['bongleshnout', 'foundlemoup', 'dingledoo', 'maxted']
    render_chars = []

    char_selected: str = ''

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
            #draw name center top of char
            font = pygame.font.SysFont('Comic Sans MS', 30)
            text = font.render(chars[i], True, (255, 255, 255))
            screen.blit(text, (-130 + render_chars[i].get_width() / 2 + (i * 300) + ((render_chars[i].get_width() - text.get_width()) / 2), screen.get_height() / 2 - render_chars[i].get_height() / 2 + 100 - text.get_height()))


    def clear_draw(iOutline: int = -1):
        #clear the screen
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('Comic Sans MS', 50)
        text = font.render('Choose your Character!', True, (255, 255, 255))
        #blit the text on the center of the screen
        screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() / 2 - text.get_height() / 2 - 300))
        draw_chars(iOutline)

    clear_draw()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in range(len(render_chars)):
                        if render_chars[i].get_rect(topleft=(-130 + render_chars[i].get_width() / 2 + (i * 300), screen.get_height() / 2 - render_chars[i].get_height() / 2 + 100)).collidepoint(event.pos):
                            char_selected = chars[i]
                            return 'versus', char_selected
                            
            if event.type == pygame.MOUSEMOTION:
                for i in range(len(render_chars)):
                    if render_chars[i].get_rect(topleft=(-130 + render_chars[i].get_width() / 2 + (i * 300), screen.get_height() / 2 - render_chars[i].get_height() / 2 + 100)).collidepoint(event.pos):
                        clear_draw(i)
                    else:
                        continue

        pygame.display.update()
