import pygame

class Toolbar:
    """
    A toolbar going from the left to the right of the screen.
    It is designed to be used with buttons.
    """
    def __init__(self, screen, height, background_color, buttons=[]):
        self.screen = screen
        self.width = self.screen.width
        self.height = height
        self.background_color = background_color

        # Buttons
        self.buttons = buttons
        self.space_per_button = self.width / len(buttons)

    def draw(self):
        """
        Draw the toolbar first, then its buttons.
        """
        pygame.draw.rect(self.screen.get_screen(), self.background_color, (0, 0, self.width, self.height))        
        self.draw_buttons()

    def draw_buttons(self):
        horizontal_space = 0
        for button in self.buttons:
            # new_x=None, new_y=None, new_width=None, new_height=None, background_color = None, label = None
            button.update(new_x = horizontal_space, new_y = 10, new_width = self.space_per_button, new_height = self.height)
            horizontal_space += self.space_per_button
            button.draw()
