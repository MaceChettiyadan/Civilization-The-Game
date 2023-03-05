import pygame
import sys
import random
from math import *

def random_name_generator(type: str):
    match type:
        case 'Place':
            #random name generator for places, using a list of prefixes and suffixes
            prefixes = ['New', 'Old', 'Great', 'Little', 'Big', 'Small', 'Upper', 'Lower', 'Middle', 'North', 'South', 'East', 'West', 'Fort', 'Fortress', 'Castle', 'City', 'Town', 'Village', 'Hamlet', 'Farm', 'Fern', 'Oak', 'Maple', 'Birch', 'Pine', 'Willow', 'Elm', 'Cedar', 'Hickory', 'Ash', 'Spruce', 'Beech', 'Holly', 'O']
            suffixes = ['town', 'ville', 'burg', 'ham', 'shire', 'land', 'ford', 'borough', 'burgh', 'port', 'mouth', 'haven', 'wick', 'ton', 'field', 'wood', 'bury', 'chester', 'fix', 'ton']
            optional_second_suffixes = ['Hills', 'Central', 'Lands', 'Downs']
            if random.randint(0, 1) == 1:
                return random.choice(prefixes) + random.choice(suffixes) + ' ' + random.choice(optional_second_suffixes)
            return random.choice(prefixes) + random.choice(suffixes)

        case 'Tribe':
            #more random names, this time using groups of syllables
            syllable_groups = [
                ['a', 'e', 'i', 'o', 'u', 'y'],
                ['ba', 'be', 'bi', 'bo', 'bu', 'by'],
                ['ca', 'ce', 'ci', 'co', 'cu', 'cy'],
                ['da', 'de', 'di', 'do', 'du', 'dy'],
                ['fa', 'fe', 'fi', 'fo', 'fu', 'fy'],
                ['ga', 'ge', 'gi', 'go', 'gu', 'gy'],
                ['ha', 'he', 'hi', 'ho', 'hu', 'hy'],
                ['ja', 'je', 'ji', 'jo', 'ju', 'jy'],
                ['ka', 'ke', 'ki', 'ko', 'ku', 'ky'],
                ['la', 'le', 'li', 'lo', 'lu', 'ly'],
                ['ma', 'me', 'mi', 'mo', 'mu', 'my'],
                ['na', 'ne', 'ni', 'no', 'nu', 'ny'],
                ['pa', 'pe', 'pi', 'po', 'pu', 'py'],
                ['ra', 're', 'ri', 'ro', 'ru', 'ry'],
                ['sa', 'se', 'si', 'so', 'su', 'sy'],
                ['ta', 'te', 'ti', 'to', 'tu', 'ty'],
                ['va', 've', 'vi', 'vo', 'vu', 'vy'],
                ['wa', 'we', 'wi', 'wo', 'wu', 'wy'],
                ['xa', 'xe', 'xi', 'xo', 'xu', 'xy'],
                ['za', 'ze', 'zi', 'zo', 'zu', 'zy'],
                ['qu', 'qu', 'qu', 'qu', 'qu', 'qu'],
                ['ch', 'ch', 'ch', 'ch', 'ch', 'ch'],
                ['sh', 'sh', 'sh', 'sh', 'sh', 'sh'],
                ['th', 'th', 'th', 'th', 'th', 'th'],
                ['ph', 'ph', 'ph', 'ph', 'ph', 'ph'],
                ['wh', 'wh', 'wh', 'wh', 'wh', 'wh'],
                ['bl', 'bl', 'bl', 'bl', 'bl', 'bl'],
                ['br', 'br', 'br', 'br', 'br', 'br'],
                ['cl', 'cl', 'cl', 'cl', 'cl', 'cl'],
                ['cr', 'cr', 'cr', 'cr', 'cr', 'cr'],
            ]
            name = ''
            for i in range(random.randint(2, 4)):
                name += random.choice(syllable_groups[random.randint(0, len(syllable_groups) - 1)])
            tribe_names = ['Barbarians', 'Berserkers', 'Savages', 'Marauders', 'Hunters', 'Archers', 'Rangers', 'Scouts', 'Aristocrats', 'Lords', 'Nobles', 'Royals', 'Warriors', 'Fighters', 'Soldiers', 'Champions', 'Defenders', 'Guardians', 'Shieldbearers', 'Wardens', 'Maelstroms','Stormbringers','Elementals','Tempests','Raiders','Explorers','Adventurers','Pirates','Knights','Paladins','Crusaders','Cavaliers', 'Druids','Shamans','Healers','Naturewalkers', 'Mages','Wizards','Sorcerers','Magicians']
            name += ' ' + random.choice(tribe_names)
            return name.capitalize()


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

def determine_coordinates(grid_position: tuple, radius: int):
    x, y = grid_position
    screen_x = 2500 + radius * 3/2 * x
    screen_y = 2500 + radius * (3**0.5) * (y + x/2)
    return (screen_x, screen_y)



class Tile:
    def __init__(self, name: str, type: str, natural_resources: int, population: int, food_capacity: int, cost: int, position: tuple, region: str, upkeep: int = 0, locked: bool = True):
        self.type = type
        self.name = name
        self.resources = natural_resources
        self.population = population
        self.food = food_capacity
        self.cost = cost
        self.is_locked = locked
        self.position = position
        self.upkeep = upkeep
        self.region = region
        self.army = floor((self.population* random.uniform(0.5, 0.8) * 0.2))
        self.income = floor((self.population * random.uniform(0.5, 0.8) * 0.1))


    def unlock(self):
        self.is_locked = False

    def is_pos_in_tile(self, pos: tuple):
        x, y = pos
        screen_x, screen_y = determine_coordinates(self.position, 50 * zoom)
        return (x - screen_x)**2 + (y - screen_y)**2 <= 50**2 * zoom**2

    def sell(self):
        if self.is_locked: return
        self.is_locked = True
        money += self.cost * (random.random())

    def render(self, selected: bool = False):
        #draw_regular_polygon(window, (255, 255, 255), 6, 50, (600 + self.position[0], 400 + self.position[1]), 50)
        draw_regular_polygon(tile_surface, (249, 224, 118), 6, 50 * zoom, determine_coordinates(self.position, 50 * zoom), outlines=True, outline_color=((255, 255, 255) if not selected else (255, 0, 0)), outline_width=4)


def draw_tooltip(tooltip, selected_buy_sell: bool = False):
    #create rectangle
    pygame.draw.rect(window, (0, 0, 0), (tooltip[1][0], tooltip[1][1], 200, 250))
    #draw text
    font = pygame.font.SysFont('Monospace', 20, bold=True)
    names = tooltip[0].name.split(' ')
    i = 0
    for i in range(len(names)):
        text = font.render(names[i], True, (255, 255, 255))
        #if two words, draw on two lines, else draw in one line in the middle
        if len(names) == 2:
            window.blit(text, (tooltip[1][0] + 100 - text.get_width() / 2, tooltip[1][1] + 10 + 20 * i))
        else:
            window.blit(text, (tooltip[1][0] + 100 - text.get_width() / 2, tooltip[1][1] + 10 + 20 * 0.5))
    #draw seperator line, dassuming 2 lines of text
    pygame.draw.line(window, (255, 255, 255), (tooltip[1][0] + 10, tooltip[1][1] + 10 + 20 * 2), (tooltip[1][0] + 190, tooltip[1][1] + 10 + 20 * 2), 2)
    fonts = pygame.sysfont.get_fonts()
    emojis = [font for font in fonts if "emoji" in font]
    font_emoji = pygame.font.SysFont(emojis[0], 20)
    text = font_emoji.render('🍉', True, (255, 255, 255))
    window.blit(text, (tooltip[1][0] + 10, tooltip[1][1] + 10 + 20 * 2 + 10))
    font = pygame.font.SysFont('Monospace', 20)
    text = font.render(str(tooltip[0].food), True, (255, 255, 255))
    window.blit(text, (tooltip[1][0] + 40, tooltip[1][1] + 10 + 20 * 2 + 10))
    text = font_emoji.render('🌲', True, (255, 255, 255))
    window.blit(text, (tooltip[1][0] + 10, tooltip[1][1] + 10 + 20 * 2 + 10 + 20))
    text = font.render(str(tooltip[0].resources), True, (255, 255, 255))
    window.blit(text, (tooltip[1][0] + 40, tooltip[1][1] + 10 + 20 * 2 + 10 + 20))
    text = font_emoji.render('👥', True, (255, 255, 255))
    window.blit(text, (tooltip[1][0] + 10, tooltip[1][1] + 10 + 20 * 2 + 10 + 20 * 2))
    text = font.render(str(tooltip[0].population), True, (255, 255, 255))
    window.blit(text, (tooltip[1][0] + 40, tooltip[1][1] + 10 + 20 * 2 + 10 + 20 * 2))
    #another seperator line
    pygame.draw.line(window, (255, 255, 255), (tooltip[1][0] + 10, tooltip[1][1] + 10 + 20 * 2 + 10 + 20 * 3.2), (tooltip[1][0] + 190, tooltip[1][1] + 10 + 20 * 2 + 10 + 20 * 3.2), 2)
    #draw upkeep
    text = font.render('Upkeep: $' + str(tooltip[0].upkeep), True, (255, 255, 255))
    window.blit(text, (tooltip[1][0] + 10, tooltip[1][1] + 10 + 20 * 2 + 10 + 20 * 3 + 10))
    #draw cost
    text = font.render(('Cost: $' if tooltip[0].is_locked else 'Value: $') + str(tooltip[0].cost), True, (255, 255, 255))
    window.blit(text, (tooltip[1][0] + 10, tooltip[1][1] + 10 + 20 * 2 + 10 + 20 * 3 + 10 + 20))
    #draw another seperator line below cost
    pygame.draw.line(window, (255, 255, 255), (tooltip[1][0] + 10, tooltip[1][1] + 10 + 20 * 2 + 10 + 20 * 4.5 + 10 + 20), (tooltip[1][0] + 190, tooltip[1][1] + 10 + 20 * 2 + 10 + 20 * 4.5 + 10 + 20), 2)
    #at the bottom right, sell/buy button
    pygame.draw.rect(window, (0, 0, 0), (tooltip[1][0] + 10, tooltip[1][1] + 10 + 20 * 2 + 10 + 20 * 4.5 + 10 + 20 + 10, 180, 50))
    #outline
    pygame.draw.rect(window, ((255, 255, 255) if not selected_buy_sell else (250,128,114)), (tooltip[1][0] + 10, tooltip[1][1] + 10 + 20 * 2 + 10 + 20 * 4.5 + 10 + 20 + 10, 180, 50), 2)
    font = pygame.font.SysFont('Monospace', 20, bold=True)
    text = font.render(('Buy' if tooltip[0].is_locked else 'Sell'), True, (255, 255, 255))
    window.blit(text, (tooltip[1][0] + 100 - text.get_width() / 2, tooltip[1][1] + 10 + 20 * 2 + 10 + 20 * 4.5 + 10 + 20 + 10 + 25 - text.get_height() / 2))
    # and now an outline for the whole thing
    pygame.draw.rect(window, (255, 255, 255), (tooltip[1][0], tooltip[1][1], 200, 10 + 20 * 2 + 10 + 20 * 5 + 10 + 20 + 10 + 50), 2)


def draw_crucial_stats(name: str):
    #rect at very bottom
    pygame.draw.rect(window, (0, 0, 0), (0, 750, 1200, 50))
    #outline
    pygame.draw.rect(window, (255, 255, 255), (0, 750, 1200, 50), 2)

    #draw city name
    font = pygame.font.SysFont('Monospace', 20, bold=True)
    text = font.render(name, True, (255, 255, 255))
    window.blit(text, (10, 750 + 25 - text.get_height() / 2))

    fonts = pygame.sysfont.get_fonts()
    emojis = [font for font in fonts if "emoji" in font]
    font_emoji = pygame.font.SysFont(emojis[0], 20)
    #draw money on right
    text = font_emoji.render('💵', True, (255, 255, 255))
    window.blit(text, (1200 - 10 - 150 - 100, 750 + 25 - text.get_height() / 2))
    text = font.render('$' + str(money), True, (255, 255, 255))
    window.blit(text, (1200 - 130 - 100, 750 + 25 - text.get_height() / 2))

    # on the right of money, draw income with a + and expenses with a -
    text = font.render('+ $' + str(income), True, (0, 255, 0))
    window.blit(text, (1200 - 10 - 50 - 10 - text.get_width(), 750 + 25 - text.get_height() / 2 - 10))
    text = font.render('- $' + str(upkeep), True, (255, 0, 0))
    window.blit(text, (1200 - 10 - 50 - 10 - text.get_width(), 750 + 25 - text.get_height() / 2 + 10))

    #draw seperator line
    pygame.draw.line(window, (255, 255, 255), (1200 - 150 - 100 - 15, 750 + 25 - 20 / 2), (1200 - 150 - 100 - 15, 750 + 25 + 20 / 2), 2)
    #draw population on right side, left of money
    text = font_emoji.render('👥', True, (255, 255, 255))
    window.blit(text, (1200 - 150 - 100 - 60 - 150 + 50, 750 + 25 - text.get_height() / 2))
    text = font.render(str(population), True, (255, 255, 255))
    window.blit(text, (1200 - 130 - 50 - 150 - 100 + 50, 750 + 25 - text.get_height() / 2))

    #draw army on right side, left of population
    text = font_emoji.render('🛡️', True, (255, 255, 255))
    window.blit(text, (1200 - 10 - 150 - 10 - 150 - 10 - 150 + 50 - 100, 750 + 25 - text.get_height() / 2))
    text = font.render(str(army), True, (255, 255, 255))
    window.blit(text, (1200 - 130 - 10 - 150 - 10 - 150  + 50- 100, 750 + 25 - text.get_height() / 2))

    #draw resources on right side, left of army
    text = font_emoji.render('🌲', True, (255, 255, 255))
    window.blit(text, (1200 - 10 - 150 - 10 - 150 - 10 - 150 + 50 - 10 - 150 - 100, 750 + 25 - text.get_height() / 2))
    text = font.render(str(resources), True, (255, 255, 255))
    window.blit(text, (1200 - 130 - 10 - 150 - 10 - 150 + 50 - 10 - 150 - 100, 750 + 25 - text.get_height() / 2))

    #draw food on right side, left of resources
    text = font_emoji.render('🍉', True, (255, 255, 255))
    window.blit(text, (1200 - 10 - 150 - 10 - 150 - 10 - 150 + 50 - 10 - 150 - 10 - 150 - 100, 750 + 25 - text.get_height() / 2))
    text = font.render(str(food), True, (255, 255, 255))
    window.blit(text, (1200 - 130 - 10 - 150 - 10 - 150 + 50 - 10 - 150 - 10 - 150 - 100, 750 + 25 - text.get_height() / 2))



def main(game, screen, name, starting_tile):
    global window
    window = screen

    global tile_surface
    tile_surface = pygame.Surface((5000, 5000))

    tile_rect = pygame.rect.Rect(0, 0, 5000, 5000)
    
    global zoom
    zoom = 4

    global money
    global population
    global army
    global resources
    global income
    global upkeep
    global food
    money = 0
    population = 0
    army = 0
    resources = 0
    income = 0
    upkeep = 0
    food = 0


    selected: Tile = None
    select_pos: tuple = (0, 0)
    dragging: bool = False

    tiles: list = [
        #the inner four. cheap and easy to get.
        Tile(random_name_generator('Place'), 'Plains', 100, 450, 450, 1000, (0, 0), 'Inner Valleys', locked=(starting_tile != 'Plains')),
        Tile(random_name_generator('Place'), 'Forests', 300, 350, 350, 1500, (1, 0), 'Inner Valleys', locked=(starting_tile != 'Forests')),
        Tile(random_name_generator('Place'), 'Mountains', 800, 150, 50, 1750, (1, 1), 'Southern Slopes', locked=(starting_tile != 'Mountains')),
        Tile(random_name_generator('Place'), 'Plains', 75, 425, 500, 1200, (0, 1), 'Inner Valleys'),
        #moving into the outer mid ranges - these tiles require some progression and upkeep
        Tile(random_name_generator('Place'), 'Mountains', 900, 75, 25, 4500, (2, 1), 'Southern Slopes', upkeep=20),
        Tile(random_name_generator('Place'), 'Forests', 300, 350, 250, 2600, (1, -1), 'Northern Forests', upkeep=22),
        Tile(random_name_generator('Place'), 'Plains', 50, 600, 350, 3200, (-1, 1), 'The Bushy Region', upkeep=16),
        Tile(random_name_generator('Place'), 'Mountains', 700, 200, 100, 5500, (2, 0), 'Southern Slopes', upkeep=19),
        Tile(random_name_generator('Place'), 'Forests', 330, 330, 340, 3200, (1, -2), 'The Bushy Region', upkeep=21)
    ]
    clock = pygame.time.Clock()
    while True:
        delta_time = clock.tick(60) / 1000
        screen.fill((0, 0, 0))
        zoom -= 0.0001
        population = 0
        army = 0
        resources = 0
        income = 0
        upkeep = 0
        food = 0

        #move tile_surface based on offset
        tile_surface.fill((0, 0, 0))

        for tile in tiles:
            if not tile.is_locked:
                #we want to earn tile.income money every second
                frac = 1 / delta_time
                money += tile.income / frac
                money = ceil(money)
                population += tile.population
                army += tile.army
                resources += tile.resources
                income += tile.income
                upkeep += tile.upkeep
                food += tile.food

            if tile == selected:
                continue
            tile.render()


        if not selected:
            window.blit(tile_surface, (tile_rect[0] - 2500, tile_rect[1] - 2500))
        else:
            selected.render(True)
            window.blit(tile_surface, (tile_rect[0] - 2500, tile_rect[1] - 2500))
            draw_tooltip((selected, select_pos))

        draw_crucial_stats(name)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                #check if we clicked on a tile
                for tile in tiles:
                    pos_offset_adjusted = (pygame.mouse.get_pos()[0] - tile_rect.x + 2500, pygame.mouse.get_pos()[1] - tile_rect.y + 2500)
                    if tile.is_pos_in_tile(pos_offset_adjusted):
                        selected = tile
                        select_pos = pygame.mouse.get_pos()
                        break
                else:
                    selected = None
                    select_pos = None

                if not selected:
                #allow for click and drag
                    dragging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = tile_rect.x - mouse_x
                    offset_y = tile_rect.y - mouse_y

            if event.type == pygame.MOUSEMOTION:
                if dragging:
                    mouse_x, mouse_y = event.pos
                    tile_rect.x = mouse_x + offset_x
                    tile_rect.y = mouse_y + offset_y

            if event.type == pygame.MOUSEBUTTONUP:
                dragging = False




        pygame.display.update()