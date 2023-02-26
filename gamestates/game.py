import textwrap
import pygame
import sys
import random

class Card:
    def __init__(self, name: str, type: str, desc: str, function, args: list, player_choose_args: bool = False, one_time: bool = True, loops_left: int = 0):
        self.name = name
        self.type = type
        self.function = function
        self.args = args
        self.in_play = False
        self.one_time = one_time
        self.loops_left = loops_left
        self.desc = desc

    def play(self):
        self.function(self.args)
        if not self.one_time: 
            self.in_play = True
            self.loops_left -= 1
            if self.loops_left == 0: del self
        else: del self

    def render(self, screen, x, y):
        screen.blit(card_template, (x, y))
        #write text
        font = pygame.font.SysFont('Comic Sans MS', 18, bold=True)
        text = font.render(self.name, True, (220,20,60) if self.type == 'attack' else ((50,205,50) if self.type == 'defence' else (0,191,255)))
        screen.blit(text, (x + 40, y + 40))

        font = pygame.font.SysFont('Comic Sans MS', 14)
        wrap_len = 12
        wrap = textwrap.wrap(self.desc, wrap_len)
        for i in range(len(wrap)):
            text = font.render(wrap[i], True, (255, 255, 255))
            screen.blit(text, (x + 40, y + 70 + i*20))

        
    def loop(self, n):
        self.one_time = False
        self.loops_left += n

    def __repr__(self):
        return f'{self.name} {self.type}'

class Player:
    def __init__(self, char: str):
        self.char = char
        self.hp = 100
        self.hand = []
        self.played = []

    def deal(self):
        match self.char:
            case 'bongleshnout':
                attack_quota = random.randint(3, 4)
                defence_quota = 7 - attack_quota
                self._dealhelper(defence_quota, attack_quota)

            case 'foundlemoup':
                defence_quota = random.randint(5, 6)
                attack_quota = 7 - defence_quota
                self._dealhelper(defence_quota, attack_quota)

            case 'dingledoo':
                attack_quota = random.randint(5, 6)
                defence_quota = 7 - attack_quota
                self._dealhelper(defence_quota, attack_quota)
                    
            case 'maxted':
                for i in range(7):
                    self.hand.append(deck[random.randint(0, len(deck) - 1)])

    def _dealhelper(self, defence_quota: int, attack_quota: int):
        #keep looping until both quotas are met
        while defence_quota > 0 or attack_quota > 0:
            random_card = deck[random.randint(0, len(deck) - 1)]
            if random_card[1] == ('defence' or 'both') and defence_quota > 0:
                self.hand.append(deck[random.randint(0, len(deck) - 1)])
                defence_quota -= 1
            elif random_card[1] == ('attack' or 'both') and attack_quota > 0:
                self.hand.append(deck[random.randint(0, len(deck) - 1)])
                attack_quota -= 1

    def damage(self, damage: int, is_percent: bool = False):
        if is_percent:
            damage = self.hp * damage
        self.hp -= damage
        #todo: add fancy visuals

    def heal(self, heal: int, is_percent: bool = False):
        if is_percent:
            heal = self.hp * heal
        self.hp += heal
        #todo: add fancy visuals
    

def main(game, screen, char: str, ai_name: str):
    screen.fill((0, 0, 0))

    global ai
    global player
    

    ai = Player(ai_name)
    player = Player(char)

    global deck
    deck = [
        [Card('Attack',
                'attack',
                'Deal 5 damage to the enemy',
                lambda args: player.damage(args[0]),
                [5]
                ), 'attack'],
        [Card('Heal',
                'defence',
                'Heal 3 health',
                lambda args: player.heal(args[0]),
                [3]
                ), 'defence'],
        [Card('Bomb',
                'attack',
                'Deal loads of damage to the enemy... but also yourself',
                lambda args: 
                    ai.damage(args[0], True)
                    and player.damage(args[1], True),
                [0.35, 0.45]
                ), 'attack'],
        [Card('Loop',
                'both',
                'Loop a card in play of your choosing',
                lambda args: 
                    args[0].loop(args[1])
                [None, None],
                True
                ), 'both'],
        [Card('Goofmobile',
                'defence',
                'Skip turn - by taking 1 damage.',
                lambda args: 
                    player.damage(1),
                []
                ), 'defence'],
    ]

    player.deal()
    ai.deal()

    player_image = pygame.image.load(f'assets/actual_art/{char}.png').convert()
    player_image = pygame.transform.scale(player_image, (player_image.get_width() / 4, player_image.get_height() / 4))
    ai_image = pygame.image.load(f'assets/actual_art/{ai_name}.png').convert()
    ai_image = pygame.transform.scale(ai_image, (ai_image.get_width() / 4, ai_image.get_height() / 4))

    global card_template
    card_template = pygame.image.load('assets/card_template.png').convert()
    card_template = pygame.transform.scale(card_template, (card_template.get_width() / 5, card_template.get_height() / 5))

    play_slot = pygame.image.load('assets/play_slot.png').convert()
    play_slot = pygame.transform.scale(play_slot, (play_slot.get_width() / 5, play_slot.get_height() / 5))
    #set opactiy of play slot
    play_slot.set_alpha(85)

    diff: int = 30

    top_card: int = None

    while True:
        if diff > 0: diff -= 1
        screen.fill((0, 0, 0))
        screen.blit(ai_image, (0, 0))
        screen.blit(player_image, (screen.get_width() - player_image.get_width(), screen.get_height() - player_image.get_height()))

        #blit play slot to the left of the player
        screen.blit(play_slot, (screen.get_width() - play_slot.get_width() - 225, screen.get_height() - 300))

        #TEXT  beneath player
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text = font.render(f'[YOU]    HP: {player.hp}', True, (255, 255, 255))
        screen.blit(text, (screen.get_width() - text.get_width() - 10, screen.get_height() - text.get_height() - 10))

        #TEXT  beneath ai
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text = font.render(f'[{ai.char.upper()}]    HP: {ai.hp}', True, (255, 255, 255))
        screen.blit(text, (10, 10))

        for i in range(len(player.hand)):
            card = player.hand[i][0]
            if i != top_card:
                card.render(screen, i * 100 + 10 - diff * i * i, screen.get_height() - 300)

        if top_card != None:
            card = player.hand[top_card][0]
            card.render(screen, top_card * 100 + 10 - diff * i * i, screen.get_height() - 350)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                #CHECK IF MOUSE IS OVER CARD
                for i in range(len(player.hand)):
                    card = player.hand[i][0]
                    if event.pos[0] > i * 100 + 10 and event.pos[0] < i * 100 + 10 + card_template.get_width():
                        if event.pos[1] > screen.get_height() - 300 and event.pos[1] < screen.get_height() - 300 + card_template.get_height():
                            top_card = i
                            break
                        else:
                            top_card = None
                    else:
                        top_card = None
        pygame.display.update()
    return 'menu'