class Team:
    def __init__(self, name, options_instance):
        self.name = name
        self.color = options_instance._player_color.get('value')
    
class TeamManager:
    """
    Manage player and enemy teams.
    """
    def __init__(self, player_name, enemy_name, options_instance):
        self.player = Team(player_name, options_instance)
        self.enemy = Team(enemy_name, options_instance)        

    def get_enemy_color(self):
        """
        WIP.
        Returns the opposite team's color.
        """
        return self.enemy.color