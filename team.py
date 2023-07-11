from color import BLUE

class Team:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_opposite_team(self):
        """
        WIP.
        Returns the opposite team's color.
        """
        return BLUE