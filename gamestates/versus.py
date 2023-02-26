import random
import pygame
import sys

def main(game, screen, char: str):
    screen.fill((0, 0, 0))
    chars: str = ['bongleshnout', 'foundlemoup', 'dingledoo', 'maxted']
    chars.remove(char)
    ai = random.choice(chars)

    you_image = pygame.image.load('assets/actual_art/' + char + '.png').convert()
    you_image = pygame.transform.scale(you_image, (you_image.get_width() / 3 , you_image.get_height() / 3))

    ai_image = pygame.image.load('assets/actual_art/' + ai + '.png').convert()
    ai_image = pygame.transform.scale(ai_image, (ai_image.get_width() / 3 , ai_image.get_height() / 3))

    versus = pygame.image.load('assets/versus.png').convert()
    versus = pygame.transform.scale(versus, (versus.get_width() / 2, versus.get_height() / 2))

    enter = pygame.image.load('assets/enterkey.png').convert()
    enter = pygame.transform.scale(enter, (enter.get_width() / 15, enter.get_height() / 15))

    you_x: int = -300
    ai_x: int = 1150
    
    draw_versus: bool = False
    while True:
        delta_time = pygame.time.Clock().tick(60) / 1000
        screen.fill((0, 0, 0))
        screen.blit(you_image, (you_x, 100))
        screen.blit(ai_image, (ai_x, 300))
        screen.blit(enter, (screen.get_width() - enter.get_width() - 50, screen.get_height() - enter.get_height() - 50))
        font = pygame.font.SysFont('Comic Sans MS', 20)
        text = font.render('[Enter] to Continue', True, (255, 255, 255))
        screen.blit(text, (screen.get_width() - text.get_width() - 50, screen.get_height() - text.get_height() - 20))
        if draw_versus:
            screen.blit(versus, (screen.get_width() / 2 - versus.get_width() / 2 - 25, screen.get_height() / 2 - versus.get_height() / 2))
            #draw text above characters
            font = pygame.font.SysFont('Comic Sans MS', 60)
            text = font.render('You (' + char + ')', True, (255, 255, 255))
            screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2 - 300, screen.get_height() / 2 - text.get_height() / 2 - 300))
            text = font.render('AI (' +ai +')', True, (255, 255, 255))
            screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2 + 300, screen.get_height() / 2 - text.get_height() / 2 - 300))

        if you_x < 225:
            you_x += 1 * delta_time * 1000
        if ai_x > 625:
            ai_x -= 1 * delta_time * 1000

        if you_x >= 225 and ai_x <= 625:
            draw_versus = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return ['game', ai]
        
        pygame.display.update()

    return ['game', ai]