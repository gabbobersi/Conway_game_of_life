class Team:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
class TeamManager:
    """
    Manage player and enemy teams.
    """
    def __init__(self, player_name, player_color, enemy_name, enemy_color):
        self.player = Team(player_name, player_color)
        self.enemy = Team(enemy_name, enemy_color)        

    def get_enemy_color(self):
        """
        WIP.
        Returns the opposite team's color.
        """
        return self.enemy.color