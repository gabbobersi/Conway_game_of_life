from color import BLACK

import pygame

class Box:
    """
    A simple box.
    """
    def __init__(self, screen, x, y, width, height, background_color):
        self.screen = screen
        self.width = width
        self.height = height
        self.background_color = background_color
        
        if not x:
            self.x = (self.window_width - self.width) // 2
        else:
            self.x = x

        if not y:
            self.y = (self.window_height - self.height) // 2
        else:
            self.y = y

        self.window_width, self.window_height = pygame.display.get_surface().get_size()

    def draw(self):
        """
        Draw the box on the screen.
        """
        settings = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, self.background_color, settings, 0)
        pygame.draw.rect(self.screen, BLACK, settings, 2)   # Draw a black border around the box

    