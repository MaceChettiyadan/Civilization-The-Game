import time
import pygame
import sys
import random
from math import *

def random_name_generator(type: str):
    match type:
        case 'Place':
            #random name generator for places, using a list of prefixes and suffixes
            prefixes = ['New', 'Old', 'Great', 'Little', 'Big', 'Small', 'Upper', 'Lower', 'Middle', 'North', 'South', 'East', 'West', 'Fort', 'Fortress', 'Castle', 'City', 'Town', 'Village', 'Hamlet', 'Farm', 'Fern', 'Oak', 'Maple', 'Birch', 'Pine', 'Willow', 'Elm', 'Cedar', 'Hickory', 'Ash', 'Spruce', 'Beech', 'Holly', 'O', 'Spear', 'Merry', 'Berry', 'Griddle', 'Fardle', 'Bongle', 'Modern', 'Silly']
            suffixes = ['town', 'ville', 'burg', 'ham', 'shire', 'land', 'ford', 'borough', 'burgh', 'port', 'mouth', 'haven', 'wick', 'ton', 'field', 'wood', 'bury', 'chester', 'fix', 'ton']
            optional_second_suffixes = ['Hills', 'Central', 'Lands', 'Downs', 'Valley', 'Shire', 'Township', 'Village', 'Haven', 'Port', 'Deltas']
            optional_second_prefixes = ['Saint', 'The', 'Holy', 'Esteemed']
            if random.randint(0, 1) == 1:
                return random.choice(prefixes) + random.choice(suffixes) + ' ' + random.choice(optional_second_suffixes)
            elif random.randint(0, 2) == 0:
                return random.choice(optional_second_prefixes) + ' ' + random.choice(prefixes) + random.choice(suffixes)
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


def draw_tile(surface, radius, position, image, width=0, outlines=False, outline_color=(0, 0, 0), outline_width=1):
    x, y = position
    screen_x = (2500 + radius * 3/2 * x)
    screen_y = (2500 + radius * (3**0.5) * (y + x/2))
    #render so that width is radius times 2, and height is scaled to match
    scale_width = radius * 2
    scale_height = radius * 2 * (image.get_height() / image.get_width())
    image = pygame.transform.scale(image, (int(scale_width), int(scale_height)))
    
    

    surface.blit(image, (screen_x - radius, screen_y - radius * 2))
    if outlines:
        #draw 6 lines to make a hexagon
        pygame.draw.line(surface, outline_color, (screen_x - radius, screen_y), (screen_x - radius/2, screen_y - radius * (3**0.5)/2), outline_width)
        pygame.draw.line(surface, outline_color, (screen_x - radius/2, screen_y - radius * (3**0.5)/2), (screen_x + radius/2, screen_y - radius * (3**0.5)/2), outline_width)
        pygame.draw.line(surface, outline_color, (screen_x + radius/2, screen_y - radius * (3**0.5)/2), (screen_x + radius, screen_y), outline_width)
        pygame.draw.line(surface, outline_color, (screen_x + radius, screen_y), (screen_x + radius/2, screen_y + radius * (3**0.5)/2), outline_width)
        pygame.draw.line(surface, outline_color, (screen_x + radius/2, screen_y + radius * (3**0.5)/2), (screen_x - radius/2, screen_y + radius * (3**0.5)/2), outline_width)
        pygame.draw.line(surface, outline_color, (screen_x - radius/2, screen_y + radius * (3**0.5)/2), (screen_x - radius, screen_y), outline_width)


def determine_coordinates(grid_position: tuple, radius: int):
    x, y = grid_position
    screen_x = 2500 + radius * 3/2 * x
    screen_y = 2500 + radius * (3**0.5) * (y + x/2)
    return (screen_x, screen_y)

class Notification:
    def __init__(self, text: str, color: tuple, time: float):
        self.text = text
        self.color = color
        self.time = time
        self.max_time = time

    def render(self, surface: pygame.Surface, position: tuple):
        #draw rect that is black with a white border
        pygame.draw.rect(surface, (0, 0, 0), (position[0] - 5, position[1] - 5, 1000, 75))        
        pygame.draw.rect(surface, (255, 255, 255), (position[0] - 5, position[1] - 5, 1000, 75), 5)
        #draw text, make sure it is perfectly centered
        font = pygame.font.SysFont('Monospace', 25, bold=True)
        text = font.render(self.text, True, self.color)
        surface.blit(text, (position[0] + 500 - text.get_width()/2, position[1] + 37.5 - text.get_height()/2))
        #draw progress bar on bottom of above rect
        pygame.draw.rect(surface, (255, 255, 255), (position[0], position[1] + 70, 990, 5))
        pygame.draw.rect(surface, (255, 0, 0), (position[0], position[1] + 70, 990 * (self.time / self.max_time), 5))

    def update(self, dt: float):
        self.time -= dt


class Tile:
    def __init__(self, name: str, type: str, natural_resources: int, population: int, food_capacity: int, cost: int, position: tuple, upkeep: int = 0, locked: bool = True):
        self.type = type
        self.name = name
        self.resources = natural_resources
        self.population = population
        self.food = food_capacity
        self.cost = cost
        self.is_locked = locked
        self.position = position
        self.upkeep = upkeep
        self.army = floor((self.population* random.uniform(0.5, 0.8)))
        self.income = floor((self.resources * random.uniform(0.5, 0.8) * 0.1))
        self.image = images[self.type][random.randint(0, len(images[self.type]) - 1)]
        self.purchasable = False
        self.adjacent_likelihood = self.adjacency_calc()
        

    def unlock(self):
        self.is_locked = False
        #get an array of 6 tuples for the 6 possible adjacent tiles
        adjacent_tiles = [
            (self.position[0] - 1, self.position[1]),
            (self.position[0] + 1, self.position[1]),
            (self.position[0], self.position[1] - 1),
            (self.position[0], self.position[1] + 1),
            (self.position[0] - 1, self.position[1] + 1),
            (self.position[0] + 1, self.position[1] - 1)
        ]
        for adjacent in adjacent_tiles:
            does_exist = False
            for tile in tiles:
                if tile.position == adjacent:
                    does_exist = True
                    break
            if not does_exist:
                #create a new tile
                name = random_name_generator('Place')
                #use adjacency calc to determine the type of the new tile
                new_type = random.choices(list(self.adjacent_likelihood.keys()), list(self.adjacent_likelihood.values()))[0]
                match new_type:
                    case 'Plains':
                        population = random.randint(0, 400)
                        food_capacity = 1000 - population - random.randint(0, 100)
                        natural_resources = 1000 - population - food_capacity
                    case 'Deserts':
                        natural_resources = 900
                        population = random.randint(0, 100)
                        food_capacity = 1000 - population - natural_resources
                    case 'Forests':
                        natural_resources = random.randint(0, 300)
                        population = 1000 - natural_resources - random.randint(0, 300)
                        food_capacity = 1000 - population - natural_resources
                    case 'Mountains':
                        natural_resources = random.randint(0, 700)
                        population = random.randint(0, 300)
                        food_capacity = 1000 - population - natural_resources
                    case 'Water':
                        natural_resources = random.randint(0, 1000)
                        population = 0
                        food_capacity = 0

                cost = floor(1000 + (abs(self.position[0]) + abs(self.position[1])) * 1000)

                #higher upkeep the further out you go, or the more resources the tile has
                upkeep = floor((abs(self.position[0]) + abs(self.position[1])) * 15 + natural_resources * 0.01)
                
                new_tile = Tile(name, new_type, natural_resources, population, food_capacity, cost, adjacent, upkeep)
                tiles.append(new_tile)

    def adjacency_calc(self):
        match self.type:
            case 'Plains':
                return {'Plains': 0.3, 'Deserts': 0.2, 'Forests': 0.3, 'Mountains': 0.1, 'Water': 0.1}
            case 'Deserts':
                return {'Plains': 0.2, 'Deserts': 0.4, 'Forests': 0.1, 'Mountains': 0.2, 'Water': 0.1}
            case 'Forests':
                return {'Plains': 0.3, 'Deserts': 0.1, 'Forests': 0.3, 'Mountains': 0.2, 'Water': 0.1}
            case 'Mountains':
                return {'Plains': 0.1, 'Deserts': 0.2, 'Forests': 0.2, 'Mountains': 0.4, 'Water': 0.1}
            case 'Water':
                return {'Plains': 0.2, 'Deserts': 0.2, 'Forests': 0.2, 'Mountains': 0, 'Water': 0.4}

    def is_pos_in_tile(self, pos: tuple):
        x, y = pos
        screen_x, screen_y = determine_coordinates(self.position, 50 * zoom)
        return (x - screen_x)**2 + (y - screen_y)**2 <= 50**2 * zoom**2

    def render(self, selected: bool = False, is_buyable: bool = False):
        if is_buyable:
            image = images['Buy'][0]
        else:
            image = self.image
        draw_tile(tile_surface, 50 * zoom, self.position, image, outlines=selected, outline_color=(255, 255, 255), outline_width=4)

def draw_tooltip(tooltip, selected_buy: bool = False):
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
    #at the bottom right, buy button
    pygame.draw.rect(window, (0, 0, 0), (tooltip[1][0] + 10, tooltip[1][1] + 10 + 20 * 2 + 10 + 20 * 4.5 + 10 + 20 + 10, 180, 50))
    #outline
    pygame.draw.rect(window, ((255, 255, 255) if not selected_buy else (250,128,114)), (tooltip[1][0] + 10, tooltip[1][1] + 10 + 20 * 2 + 10 + 20 * 4.5 + 10 + 20 + 10, 180, 50), 2)
    font = pygame.font.SysFont('Monospace', 20, bold=True)
    text = font.render(('[ENTER] Buy' if tooltip[0].is_locked else '[ENTER] Close'), True, (255, 255, 255))
    window.blit(text, (tooltip[1][0] + 100 - text.get_width() / 2, tooltip[1][1] + 10 + 20 * 2 + 10 + 20 * 4.5 + 10 + 20 + 10 + 25 - text.get_height() / 2))
    # and now an outline for the whole thing
    pygame.draw.rect(window, (255, 255, 255), (tooltip[1][0], tooltip[1][1], 200, 10 + 20 * 2 + 10 + 20 * 5 + 10 + 20 + 10 + 50), 2)


def draw_crucial_stats(name: str, money: int):
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
    text = font.render('$' + str(floor(money)), True, (255, 255, 255))
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

def get_rand_description(type: str, title: str):
    match type:
        case 'Invasion':
            choices = [
                'The ' + title + ' have invaded your lands! They seek to take ' + random.choice(['your resources and your people', 'everything you have', 'your livelihood', 'your people']) +', and stopping them is essential to your survival. The ' + title + ' are a ' + random.choice(['cunning', 'powerful', 'loyal', 'extreme', 'brutal', 'aggressive']) + ' force.',
                'Well done player, for you have grown mighty enough to see your empire threatened. The ' + title + ' seek to invade your lands, and take '  + random.choice(['your resources and your people', 'everything you have', 'your livelihood', 'your people']) + '. To deter them is to ensure your survival.',
                'From lands foreign to ours, the ' + title + ' seek to invade us. To wreak havoc, to take ' + random.choice(['our resources and our people', 'everything we have', 'our livelihood', 'our people']) + '. As the leader of these lands, you must stop them. They are a ' + random.choice(['cunning', 'powerful', 'loyal', 'extreme', 'brutal', 'aggressive']) + ' force.',
            ]
            return random.choice(choices)
        case 'Natural Disaster':
            choices = [
                'A long spell of drought has struck your lands, and your people are suffering. You must find a way to provide for them, or they will perish.',
                'Floods have wreaked havoc on the ' + random.choice(['northwest territories', 'southern lands', 'eastern plains']) + ', and they continue to expand. You must stop this and ensure that the food supply remains secure, and the people do not get washed away to oblivion.',
                'A rather large hurricane is headed your way. Set to strike ' + random.choice(tiles).name + ', it will cause a lot of damage. You must ensure that your people are safe, and that the damage is kept to a minimum.',
                'The tribe of ' + random_name_generator('Tribe') + ' has been struck by a terrible plague. A key trading partner, we have been forced to cease all trade with them, but the disease stays rampant. Only money can stop it now.',
                'A terrible earthquake has struck the ' + random.choice(['northwest territories', 'southern lands', 'eastern plains']) + ', and it has caused a lot of damage. You must ensure that your people are safe, and that the damage is kept to a minimum.',
            ]
            return random.choice(choices)

def draw_notification(title: str, type: str, desc: str, image: str):
    #draw a rect in middle of screen
    pygame.draw.rect(window, (0, 0, 0), (600 - 300, 400 - 150, 600, 300))
    pygame.draw.rect(window, (255, 255, 255), (600 - 300, 400 - 150, 600, 300), 2)
    #draw in top center
    #draw a seperator, not full width
    pygame.draw.line(window, (255, 255, 255), (600 - 300 + 10, 400 - 150 + 10 + 25 + 10), (600 + 300 - 10, 400 - 150 + 10 + 25 + 10), 2)
    font = pygame.font.SysFont('Monospace', 20)
    length = 45
    #split the description into 20 character lines, making sure to not split words
    desc = desc.split(' ')
    desc2 = []
    for word in desc:
        if len(word) > length:
            desc2.append(word[:length])
            desc2.append(word[length:])
        else:
            desc2.append(word)
    desc = desc2
    desc2 = []
    line = ''
    for word in desc:
        if len(line) + len(word) > length:
            desc2.append(line)
            line = word
        else:
            line += ' ' + word
    desc2.append(line)
    desc = desc2
    #draw the description
    for i in range(len(desc)):
        text = font.render(desc[i], True, (255, 255, 255))
        window.blit(text, (600 - 300 + 10, 400 - 150 + 10 + 25 + 10 + 10 + 20 * i))

    match type:
        case 'Natural Disaster':
            options = ['[P] Pay for Damages']
            #draw seperator, 3/5 width
            pygame.draw.line(window, (255, 255, 255), (600 - 300 + 10, 400 - 150 + 10 + 25 + 10 + 10 + 20 * len(desc) + 10), (600 - 300 + 10 + 600 * 3 / 5, 400 - 150 + 10 + 25 + 10 + 10 + 20 * len(desc) + 10), 2)
            font = pygame.font.SysFont('Monospace', 25, bold=True)
            text = font.render(title, True, (255, 255, 255))
            window.blit(text, (600 - text.get_width() / 2, 400 - 150 + 10))
        case 'Invasion':
            font = pygame.font.SysFont('Monospace', 25, bold=True)
            text = font.render('The ' + title + ' are attacking!', True, (255, 255, 255))
            window.blit(text, (600 - text.get_width() / 2, 400 - 150 + 10))
            options = ['[B] Bribe', '[F] Fight']
            pygame.draw.line(window, (255, 255, 255), (600 - 300 + 10, 400 - 150 + 10 + 25 + 10 + 10 + 20 * len(desc) + 10), (600, 400 - 150 + 10 + 25 + 10 + 10 + 20 * len(desc) + 10), 2)
            image_render = pygame.image.load(image)
            image_render = pygame.transform.scale(image_render, (150, 100))
            window.blit(image_render, (600 - 300 + 400, 400 - 150 + 10 + 25 + 20 * len(desc) + 10 + 30 + 10))
            #draw tribe name above image
            font = pygame.font.SysFont('Monospace', 20, bold=True)
            text = font.render(title, True, (255, 255, 255))
            window.blit(text, (600 - 300 + 400 + 75 - text.get_width() / 2, 400 - 150 + 25 + 20 * len(desc) + 10 + 30 + 10 - 20))

    #draw the options
    for i in range(len(options)):
        key = options[i].split(' ')[0]
        value = options[i].split(' ')[1]
        font = pygame.font.SysFont('Monospace', 23, bold=True)
        text = font.render(key, True, (255, 255, 255))
        window.blit(text, (600 - 300 + 15, 400 - 150 + 10 + 25 + 10 + 10 + 20 * len(desc) + 30 + 30 * i))
        font = pygame.font.SysFont('Monospace', 23)
        text = font.render(value, True, (255, 255, 255))
        window.blit(text, (600 - 300 + 15 + 40, 400 - 150 + 10 + 25 + 10 + 10 + 20 * len(desc) + 30 + 30 * i))


def main(game, screen, name, starting_tile):
    #here we define all necessary global variables.
    global window
    window = screen #window is a constant

    global tile_surface
    tile_surface = pygame.Surface((5000, 5000)) #this is also a constant; a surface to render the tiles onto

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

    money = 3000
    population = 0
    army = 0
    resources = 0
    income = 0
    upkeep = 0
    food = 0

    global images
    images = {
        'Plains': [pygame.image.load('assets/plains/plains1.png').convert_alpha(), pygame.image.load('assets/plains/plains2.png').convert_alpha(), pygame.image.load('assets/plains/plains0.png').convert_alpha(), pygame.image.load('assets/plains/plains3.png').convert_alpha()],
        'Forests': [pygame.image.load('assets/forests/forests0.png').convert_alpha(), pygame.image.load('assets/forests/forests1.png').convert_alpha(), pygame.image.load('assets/forests/forests2.png').convert_alpha(), pygame.image.load('assets/forests/forests3.png').convert_alpha()],
        'Mountains': [pygame.image.load('assets/mountains/mountains0.png').convert_alpha()],
        'Deserts': [pygame.image.load('assets/deserts/deserts0.png').convert_alpha(), pygame.image.load('assets/deserts/deserts1.png').convert_alpha(), pygame.image.load('assets/deserts/deserts2.png').convert_alpha(), pygame.image.load('assets/deserts/deserts3.png').convert_alpha(), pygame.image.load('assets/deserts/deserts4.png').convert_alpha()],
        'Water': [pygame.image.load('assets/water/water0.png').convert_alpha()],
        'Buy': [pygame.image.load('assets/BuySquare.png').convert_alpha()],
    }


    selected: Tile = None
    select_pos: tuple = (0, 0)
    dragging: bool = False
    current_invasion_or_disaster: tuple = None
    starvation_timer = 30 * 60
    bankrupcy_timer = 30 * 60

    global tiles
    tiles = [
        #the inner four. cheap and easy to get.
        Tile(random_name_generator('Place'), 'Plains', 100, 450, 450, 1000, (0, 0), locked=(starting_tile != 'Plains')),
        Tile(random_name_generator('Place'), 'Forests', 300, 350, 350, 1500, (1, 0), locked=(starting_tile != 'Forests')),
        Tile(random_name_generator('Place'), 'Mountains', 600, 200, 200, 1750, (0, -1), locked=(starting_tile != 'Mountains')),
        Tile(random_name_generator('Place'), 'Deserts', 75, 425, 500, 1200, (0, 1), locked=(starting_tile != 'Deserts')),
        #moving into the outer mid ranges - these tiles require some progression and upkeep
        Tile(random_name_generator('Place'), 'Forests', 300, 350, 250, 2600, (1, -1), upkeep=22),
        Tile(random_name_generator('Place'), 'Plains', 50, 600, 350, 3200, (-1, 1), upkeep=16),
        Tile(random_name_generator('Place'), 'Forests', 300, 400, 300, 1500, (-1, 0), upkeep=18),
    ]
    clock = pygame.time.Clock()

    notifications = [
        Notification(str(random.randint(100, 900)) + 'AD: ' + name + ' has been founded!', (255, 255, 255), 5),
        Notification('Hi Mr Chillapa; this is a quality game!', (255, 255, 255), 10),
    ]

    while True:
        screen.fill((0, 0, 0))
        if zoom < 0.1:
            zoom = 0.1
        delta_time = clock.tick(60) / 1000
        population = 0
        army = 0
        resources = 0
        income = 0
        upkeep = 0
        food = 0

        #move tile_surface based on offset
        tile_surface.fill((0, 0, 0))

        #sort tiles so that lower position[1] tiles are rendered first
        tiles.sort(key=lambda x: x.position[1])

        for tile in tiles:
            if not tile.is_locked:
                population += tile.population
                army += tile.army
                resources += tile.resources
                income += tile.income
                upkeep += tile.upkeep
                food += tile.food

            if tile == selected:
                continue
            if tile.is_locked:
                rendered = False
                #check if tile is adjacent to a tile we own
                for other_tile in tiles:
                    if other_tile.is_locked or other_tile == tile:
                        continue
                    q1 = tile.position[0]
                    r1 = tile.position[1]
                    q2 = other_tile.position[0]
                    r2 = other_tile.position[1]
                    if abs(q1 - q2) <= 1 and abs(r1 - r2) <= 1 and abs(-q1 - r1 + q2 + r2) <= 1:
                        tile.purchasable = True
                        if not rendered:
                            tile.render(is_buyable=True)
                            rendered = True
                        break

            elif not tile.is_locked:
                tile.render()

        frac = 1 / delta_time
        diff = (income - upkeep) / frac
        money += diff

        if food < population * 0.8: 
            if not any(['starving' in notification.text for notification in notifications]):
                notifications.append(Notification('Your people are starving: ' + str(floor(starvation_timer/60)) + ' seconds left.', (255, 0, 0), 10))
            else:
                #remove old notification
                for notification in notifications:
                    if 'starving' in notification.text:
                        notifications.remove(notification)
                        break
                notifications.append(Notification('Your people are starving: ' + str(floor(starvation_timer/60)) + ' seconds left.', (255, 0, 0), 10))
            starvation_timer -= delta_time * 60
            if starvation_timer <= 0:
                return 'game_over', 'Starvation'
        else:
            starvation_timer += delta_time * 60 if starvation_timer < 30 * 60 else 0
            
        if money < 0:
            #check if notification with title includes 'Bankruptcy'
            if not any(['Bankrupt' in notification.text for notification in notifications]):
                notifications.append(Notification('You are going Bankrupt: ' + str(floor(bankrupcy_timer/60)) + ' seconds left.', (255, 0, 0), 10))
            else:
                #remove old notification
                for notification in notifications:
                    if 'Bankrupt' in notification.text:
                        notifications.remove(notification)
                        break
                notifications.append(Notification('You are going Bankrupt: ' + str(floor(bankrupcy_timer/60)) + ' seconds left.', (255, 0, 0), 10))
            bankrupcy_timer -= delta_time * 60
            if bankrupcy_timer <= 0:
                return 'game_over', 'Bankruptcy'
        else:
            bankrupcy_timer += delta_time * 60 if bankrupcy_timer < 30 * 60 else 0

        if not selected:
            window.blit(tile_surface, (tile_rect[0] - 2500, tile_rect[1] - 2500))
        else:
            selected.render(True, is_buyable=selected.purchasable)
            window.blit(tile_surface, (tile_rect[0] - 2500, tile_rect[1] - 2500))
            draw_tooltip((selected, select_pos))
            
        if current_invasion_or_disaster == None and random.randint(0, 60 * 90) == 0:
            rand = random.randint(1, 10)
            path = 'assets/tribes/' + str(rand) + '.png'
            tribe_name = random_name_generator('Tribe')
            type_of_event = random.choice(['Invasion', 'Natural Disaster'])
            if type_of_event == 'Invasion':
                current_invasion_or_disaster = ('Invasion', path, tribe_name, get_rand_description('Invasion', tribe_name))
            elif type_of_event == 'Natural Disaster':
                current_invasion_or_disaster = ('Natural Disaster', path, random.choice(['A tragedy hath occured!', 'Forces of nature interfere!', 'Natural Disaster wreaks havoc!', 'Nature becomes the enemy!']), get_rand_description('Natural Disaster', tribe_name))


        if current_invasion_or_disaster != None:
            draw_notification(current_invasion_or_disaster[2], current_invasion_or_disaster[0], current_invasion_or_disaster[3], current_invasion_or_disaster[1])

        i = 0
        for notification in notifications:
            notification.render(
                window,
                #top of the screen
                (window.get_width() / 2 - 500, 50 + i * 100),
            )
            notification.update(delta_time)
            if notification.time < 0:
                notifications.remove(notification)
                del notification
            i += 1

        draw_crucial_stats(name, money)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    zoom += 0.1
                elif event.button == 5:
                    zoom -= 0.1
                else:
                #check if we clicked on a tile
                    for tile in tiles:
                        pos_offset_adjusted = (pygame.mouse.get_pos()[0] - tile_rect.x + 2500, pygame.mouse.get_pos()[1] - tile_rect.y + 2500)
                        if tile.is_pos_in_tile(pos_offset_adjusted) and (not tile.is_locked or tile.purchasable):
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

            if event.type == pygame.KEYDOWN:
                #check if pressed enter
                if event.key == pygame.K_RETURN:
                    if selected:
                        if selected.purchasable and money >= selected.cost:
                            selected.unlock()
                            selected.purchasable = False
                            money -= selected.cost
                            selected.render()
                            selected = None
                            select_pos = None
                        elif selected.purchasable and money < selected.cost:
                            notifications.append(Notification('You do not have enough money to purchase this tile!', (255, 0, 0), 5))
                            selected = None
                            select_pos = None
                        elif not selected.is_locked:
                            selected = None
                            select_pos = None
                
                if current_invasion_or_disaster != None:
                    #bfcp
                    if current_invasion_or_disaster[0] == 'Invasion':
                        #if b
                        if event.key == pygame.K_b:
                            #deduct upkeep
                            bribe = upkeep * random.random()
                            notifications.append(Notification('You have paid ' + str(bribe) + ' to the invaders!', (255, 255, 255), 5))
                            money -= bribe
                            current_invasion_or_disaster = None
                        #if f
                        if event.key == pygame.K_f:
                            #if army is between 70% and 100% of the population, walk away
                            if population * 0.7 <= army:
                                notifications.append(Notification('You have successfully defended your empire!', (255, 255, 255), 5))
                                current_invasion_or_disaster = None
                            else:
                                notifications.append(Notification('You do not have enough army units to defend your empire!', (255, 0, 0), 5))
                                return "game_over", "Invasion (not enough army units)"

                    elif current_invasion_or_disaster[0] == 'Natural Disaster' and event.key == pygame.K_p:
                        #deduct upkeep
                        loss = upkeep * random.random()
                        notifications.append(Notification('You have paid ' + str(loss) + ' due to the natural disaster!', (255, 255, 255), 5))
                        money -= loss
                        current_invasion_or_disaster = None


        pygame.display.update()