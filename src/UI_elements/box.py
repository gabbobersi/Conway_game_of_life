import pygame

from UI_elements.color import BLACK
from base_classes.entity import InteractiveEntity

class Box(InteractiveEntity):
    """
    A simple box.
    """
    def __init__(self, screen, x, y, width, height, background_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.window_width, self.window_height = pygame.display.get_surface().get_size()
        self.background_color = background_color

    def draw(self):
        """
        Draw the box on the screen.
        """
        settings = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, self.background_color, settings, 0)
        pygame.draw.rect(self.screen, BLACK, settings, 2)   # Draw a black border around the box

    