from UI_elements.color import Color

TOOLBARS = [
    {'name': 'Top', 'value': 'top'},
    {'name': 'Left', 'value': 'left'}
]

RESOLUTIONS = [
    {'name': 'HD', 'value': (1280, 720)},
    {'name': 'Medium', 'value': (960, 540)},
    {'name': 'Mini', 'value': (640, 360)}
]

TICK_SPEEDS = [
    {'name': 'Slow', 'value': 10},
    {'name': 'Medium', 'value': 20},
    {'name': 'Fast', 'value': 40}
]

PLAYER_COLORS = [
    {'name': 'Red', 'value': Color.CUSTOM_RED.value},
    {'name': 'Green', 'value': Color.CUSTOM_GREEN.value},
    {'name': 'Black', 'value': Color.CUSTOM_BLACK.value}
]

class Options:
    """
    Options available in the game. This class is a singleton.\n
    To set an option:
        >>> options.attribute = value
    
    To get an option:
        >>> options._attribute
    """
    def __init__(self):
        self.toolbar_generator = cycler(TOOLBARS)
        self.resolution_generator = cycler(RESOLUTIONS)
        self.tick_speed_generator = cycler(TICK_SPEEDS)
        self.player_generator = cycler(PLAYER_COLORS)
    
    _instance = None
    _tick_speed = TICK_SPEEDS[0]
    _toolbar_position = TOOLBARS[0]
    _player_color = PLAYER_COLORS[0]
    _enemy_color = Color.CUSTOM_BLUE.value
    _resolution = RESOLUTIONS[0]

    @property
    def tick_speed(self):
        self._tick_speed = self.tick_speed_generator.__next__()
        return self._tick_speed
    
    @tick_speed.setter
    def tick_speed(self, value:int):
        self._tick_speed = value

    @property
    def toolbar_position(self):
        self._toolbar_position = self.toolbar_generator.__next__()
        return self._toolbar_position
    
    @toolbar_position.setter
    def toolbar_position(self, value:str):
        if value not in ('top', 'left'):
            print("Error :: Invalid toolbar position {}".format(value))
            self._toolbar_position = 'top'
            return
        key = self._toolbar_position.get('name')
        [toolbar for toolbar in TOOLBARS if toolbar.get('name') == key][0].update({'name': key, 'value': value})

    @property
    def player_color(self):
        self._player_color = self.player_generator.__next__()
        return self._player_color
    
    @player_color.setter
    def player_color(self, value:tuple[int, int, int]):
        self._player_color = value

    @property
    def enemy_color(self):
        return self._enemy_color
    
    @enemy_color.setter
    def enemy_color(self, value:tuple[int, int, int]):
        self._enemy_color = value
    
    @property
    def resolution(self):
        self._resolution = self.resolution_generator.__next__()
        return self._resolution
    
    @resolution.setter
    def resolution(self, value:tuple[int, int, int]):
        self._resolution = value

    # Singleton
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
    
