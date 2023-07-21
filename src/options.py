from UI_elements.color import *
class Options:
    """
    Options available in the game.
    """
    _tick_speed = 10
    _toolbar_position = 'top'
    _player_color = CUSTOM_RED
    _enemy_color = CUSTOM_BLUE
    _resolution = (1280, 720)

    @property
    def tick_speed(self):
        return self._tick_speed
    
    @tick_speed.setter
    def tick_speed(self, value):
        self._tick_speed = value

    @property
    def toolbar_position(self):
        return self._toolbar_position
    
    @toolbar_position.setter
    def toolbar_position(self, value):
        if value not in ('top', 'left'):
            print("Error :: Invalid toolbar position {}".format(value))
            self._toolbar_position = 'top'
            return
        self._toolbar_position = value
        
    @property
    def player_color(self):
        return self._player_color
    
    @player_color.setter
    def player_color(self, value):
        self._player_color = value

    @property
    def enemy_color(self):
        return self._enemy_color
    
    @enemy_color.setter
    def enemy_color(self, value):
        self._enemy_color = value
    
    @property
    def resolution(self):
        return self._resolution
    
    @resolution.setter
    def resolution(self, value):
        self._resolution = value