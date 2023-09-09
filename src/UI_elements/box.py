import pygame

from UI_elements.color import Color
from UI_elements.base_classes.entity import InteractiveEntity

class Box(InteractiveEntity):
    """
    A simple box.
    """
    def __init__(self, screen:pygame.Surface, x:int, y:int, width:int, height:int, background_color:tuple[int, int, int]):
        super().__init__(x, y, width, height)
        self.screen = screen
        self.background_color = background_color

    def draw(self):
        """
        Draw the box on the screen.
        """
        settings = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, self.background_color, settings, 0)
        pygame.draw.rect(self.screen, Color.BLACK.value, settings, 1)   # Draw a black border around the box

    def update(self, new_x:int, new_y:int, new_width:int, new_height:int, new_background_color:tuple[int, int, int]):
        """
        Update box's attributes.
        """
        if new_x:
            self.x = new_x
        if new_y:
            self.y = new_y
        if new_width:
            self.width = new_width
        if new_height:
            self.height = new_height
        if new_background_color:
            self.background_color = new_background_color
