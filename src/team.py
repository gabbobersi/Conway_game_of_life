from options import Options

class Team:
    def __init__(self, name:str, color:tuple[int, int, int]):
        self.name = name
        self.color = color
    
class TeamManager:
    """
    Manage player and enemy teams.
    """
    def __init__(self, player_name:str, enemy_name:str, options_instance:Options):
        self.player = Team(player_name, options_instance.get_actual_value('player_color').get('value'))
        self.enemy = Team(enemy_name, options_instance.get_actual_value('enemy_color').get('value'))