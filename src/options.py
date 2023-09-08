from UI_elements.color import Color
from screen import Screen

import pygame


class OptionsData:
    # First element of each list is the default one
    TOOLBARS = {
        'default': None,
        'available_values': [
            {'name': 'Top', 'value': 'top'},
            {'name': 'Left', 'value': 'left'}
        ] 
    }
    RESOLUTIONS = {
        'default': None,
        'available_values': [
            {'name': 'HD', 'value': (1280, 720)},
            {'name': 'Medium', 'value': (960, 540)},
            {'name': 'Mini', 'value': (640, 360)}
        ]
    }
    TICK_SPEEDS = {
        'default': None,
        'available_values': [
            {'name': 'Slow', 'value': 10},
            {'name': 'Medium', 'value': 20},
            {'name': 'Fast', 'value': 40}
        ]
    }

    PLAYER_COLORS = {
        'default': None,
        'available_values': [
            {'name': 'Red', 'value': Color.CUSTOM_RED.value},
            {'name': 'Green', 'value': Color.CUSTOM_GREEN.value},
            {'name': 'Black', 'value': Color.CUSTOM_BLACK.value}
        ]
    }

    ENEMY_COLORS = {
        'default': None,
        'available_values': [
            {'name': 'Blue', 'value': Color.CUSTOM_BLUE.value},
            {'name': 'Yellow', 'value': Color.CUSTOM_YELLOW.value},
            {'name': 'White', 'value': Color.CUSTOM_WHITE.value}
        ]
    }

    def __init__(self) -> None:
        # Setting default values
        self.TOOLBARS['default'] = self.TOOLBARS['available_values'][0]
        self.RESOLUTIONS['default'] = self.RESOLUTIONS['available_values'][0]
        self.TICK_SPEEDS['default'] = self.TICK_SPEEDS['available_values'][0]
        self.PLAYER_COLORS['default'] = self.PLAYER_COLORS['available_values'][0]
        self.ENEMY_COLORS['default'] = self.ENEMY_COLORS['available_values'][0]


class Options:
    """
    Options available in the game. This class is a singleton.\n
    """
    def __init__(self):
        self.__data = OptionsData()
        self.__toolbar_generator = cycler(self.__data.TOOLBARS['available_values'])
        self.__resolution_generator = cycler(self.__data.RESOLUTIONS['available_values'])
        self.__tick_speed_generator = cycler(self.__data.TICK_SPEEDS['available_values'])
        self.__player_color_generator = cycler(self.__data.PLAYER_COLORS['available_values'])
        self.__enemy_color_generator = cycler(self.__data.ENEMY_COLORS['available_values'])

        self.__toolbar_position = self.__data.TOOLBARS['default']
        self.__resolution = self.__data.RESOLUTIONS['default']
        self.__tick_speed = self.__data.TICK_SPEEDS['default']
        self.__player_color = self.__data.PLAYER_COLORS['default']
        self.__enemy_color = self.__data.ENEMY_COLORS['default']

        self.clock = pygame.time.Clock()
        self.window_width, self.window_height = self.get_actual_value('resolution').get('value')
        self.screen = Screen(self.window_width, self.window_height)
        self.cell_size = 10

    def clock_tick(self):
        self.clock.tick(self.__tick_speed.get('value'))

    def get_actual_value(self, element):
        if element == 'toolbar':
            return self.__toolbar_position
        elif element == 'resolution':
            return self.__resolution
        elif element == 'tick_speed':
            return self.__tick_speed
        elif element == 'player_color':
            return self.__player_color
        elif element == 'enemy_color':
            return self.__enemy_color
        else:
            raise ValueError('Invalid element')
        
    def get_next_value(self, element):
        if element == 'toolbar':
            self.__toolbar_position = self.get_different_value('toolbar')            
            return self.__toolbar_position
        elif element == 'resolution':
            self.__resolution = self.get_different_value('resolution')
            return self.__resolution
        elif element == 'tick_speed':
            self.__tick_speed = self.get_different_value('tick_speed')
            return self.__tick_speed
        elif element == 'player_color':
            self.__player_color = self.get_different_value('player_color')
            return self.__player_color
        elif element == 'enemy_color':
            self.__enemy_color = self.get_different_value('enemy_color')
            return self.__enemy_color
        else:
            raise ValueError('Invalid element')

    def get_different_value(self, element):
            generator_attribute_name = f'_{self.__class__.__name__}__{element}_generator'

            old = getattr(self, generator_attribute_name)
            if not old:
                raise ValueError('Invalid element')
            new = next(getattr(self, generator_attribute_name))

            # If the actual element is equal the new one, i return the next one again (to get a different value)
            if old == new:
                return next(getattr(self, generator_attribute_name)) 
            return new

    def set_value(self, element, value):
        if element == 'toolbar':
            self.__toolbar_position = value
        elif element == 'resolution':
            self.__resolution = value
        elif element == 'tick_speed':
            self.__tick_speed = value
        elif element == 'player_color':
            self.__player_color = value
        elif element == 'enemy_color':
            self.__enemy_color = value
        else:
            raise ValueError('Invalid element')

    # Singleton
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Options, cls).__new__(cls)
            cls._instance.value = None
        return cls._instance


def cycler(iterable):
    """
    Cycles all the elements of an iterable from the firt to the last. Then it restarts from the first.
    """
    index = 0
    length = len(iterable)

    while True:
        yield iterable[index]
        index = (index + 1) % length
    
