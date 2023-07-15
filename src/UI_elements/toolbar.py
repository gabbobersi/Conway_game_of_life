import pygame

SETTINGS = {
    'top_toolbar': {
        'height': 50
    },
    'left_side_toolbar': {
        'width': 200
    }
}


class Toolbar:
    """
    A simple toolbar with no orientation.
    It should not be used without orientation (so it should not be used directly).
    """
    def __init__(self, screen, width, height, background_color, buttons=[]):
        self.screen = screen
        self.width = width
        self.height = height
        self.background_color = background_color
        # Buttons
        self.buttons = buttons

    def draw(self):
        """
        Draw the toolbar.
        """
        pygame.draw.rect(self.screen.get_screen(), self.background_color, (0, 0, self.width, self.height))     

class TopToolbar(Toolbar):
    """
    A toolbar going from the top left to the top right of the screen.
    It is designed to be used with buttons.
    """
    def __init__(self, screen, height, background_color, buttons=[]):
        width = screen.width
        super().__init__(screen, width, height, background_color, buttons)
        self.space_per_button = width / len(buttons)

    def draw(self):
        """
        Draw the toolbar first, then its buttons.
        """
        super().draw()
        self.draw_buttons()

    def draw_buttons(self):
        horizontal_space = 0
        for button in self.buttons:
            # new_x=None, new_y=None, new_width=None, new_height=None, background_color = None, label = None
            button.update(new_x = horizontal_space, new_y = 0, new_width = self.space_per_button, new_height = self.height)
            horizontal_space += self.space_per_button
            button.draw()

class LeftSideToolbar(Toolbar):
    """
    A toolbar going from the top left to the bottom left of the screen.
    It is designed to be used with buttons.
    """
    def __init__(self, screen, width, background_color, buttons=[]):
        height = screen.height
        super().__init__(screen, width, height, background_color, buttons)
        self.space_per_button = height / len(buttons)

    def draw(self):
        """
        Draw the toolbar first, then its buttons.
        """
        super().draw()
        self.draw_buttons()

    def draw_buttons(self):
        vertical_space = 0
        for button in self.buttons:
            # new_x=None, new_y=None, new_width=None, new_height=None, background_color = None, label = None
            button.update(new_x = 0, new_y = vertical_space, new_width = self.width, new_height = self.space_per_button)
            vertical_space += self.space_per_button
            button.draw()
