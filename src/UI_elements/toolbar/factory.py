from .commons import VALID_TOOLBARS
from .toolbar import TopToolbar, LeftSideToolbar

class ToolbarFactory:
    """
    This class should be used to dinamically create toolbars instances.
    """
    def __init__(self, screen, background_color, buttons, labels):
        self.screen = screen
        self.background_color = background_color
        self.buttons = buttons
        self.labels = labels

    def get_instance(self, type_of_toolbar):
        if type_of_toolbar == 'top':
            return TopToolbar(self.screen, self.background_color, self.buttons, self.labels)
        elif type_of_toolbar == 'left':
            return LeftSideToolbar(self.screen, self.background_color, self.buttons, self.labels)
        else:
            raise ValueError("Error :: Invalid toolbar type {}. Valid types are: {}".format(type_of_toolbar, VALID_TOOLBARS))