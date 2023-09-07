"""
Toolbars are created with a factory. They should not be used directly.
"""
import pygame
from .commons import SETTINGS

class Toolbar:
    """
    A simple toolbar with no orientation.
    It should not be used directly.
    """
    def __init__(self, screen, width, height, background_color, buttons, labels):
        self.screen = screen
        self.width = width
        self.height = height
        self.background_color = background_color
        self.buttons = buttons
        self.labels = labels

    def draw(self):
        """
        Draw the toolbar.
        """
        pygame.draw.rect(self.screen.get_screen(), self.background_color, (0, 0, self.width, self.height))     


class TopToolbar(Toolbar):
    """
    A toolbar going from the top left to the top right of the screen.
    It should not be used directly.
    """
    def __init__(self, screen, background_color, buttons, labels):
        height = SETTINGS['top']['height']
        super().__init__(screen, screen.width, height, background_color, buttons, labels)
        self.space_per_button = screen.width / len(buttons)
        self.labels_starting_x = 20
        self.labels_starting_y = height + 5
        self.label_x = SETTINGS['top']['label_position']['additional_x']
        self.label_y = SETTINGS['top']['label_position']['additional_y']

    def draw(self):
        """
        Draw the toolbar first, then its buttons.
        """
        super().draw()
        self.__draw_buttons()
        self.__draw_labels()

    def __draw_buttons(self):
        horizontal_space = 0
        for button in self.buttons:
            # new_x=None, new_y=None, new_width=None, new_height=None, background_color = None, label = None
            button.update(new_x = horizontal_space, new_y = 0, new_width = self.space_per_button, new_height = self.height)
            horizontal_space += self.space_per_button
            button.draw()

    def __draw_labels(self):
        y_offset = 0
        for label in self.labels:
            label.update(new_x = self.labels_starting_x + self.label_x, 
                         new_y = self.labels_starting_y + self.label_y + y_offset)
            y_offset += 30
            label.draw()


class LeftSideToolbar(Toolbar):
    """
    A toolbar going from the top left to the bottom left of the screen.
    It should not be used directly.
    """
    def __init__(self, screen, background_color, buttons, labels):
        width = SETTINGS['left']['width']
        super().__init__(screen, width, screen.height, background_color, buttons, labels)
        self.space_per_button = screen.height / len(buttons)

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

    def draw_labels(self):
        offset = 1
        for label in self.labels:
            label.update(new_x = label.get_label_position()[0] * offset, new_y = self.height + label.get_label_position()[1])
            label.draw()
            offset += 1

    def get_label_position(self):
        position = SETTINGS['left']['label_position']
        return (position['additional_x'], position['additional_y'])