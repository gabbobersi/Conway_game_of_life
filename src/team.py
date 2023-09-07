from options import Options

class Team:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
class TeamManager:
    """
    Manage player and enemy teams.
    """
    def __init__(self, player_name:str, enemy_name:str, options_instance:Options):
        self.player = Team(player_name, options_instance._player_color.get('value'))
        self.enemy = Team(enemy_name, options_instance._enemy_color)