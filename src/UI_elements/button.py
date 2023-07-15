import pygame
from UI_elements.color import *
from UI_elements.box import Box

class Button(Box):
    """
    A simple box with a labels on it. It can be clicked.
    """
    def __init__(self, screen, label = '', visible = False, x=None, y=None, width=100, height=50, background_color=CUSTOM_RED):
        super().__init__(screen, x, y, width, height, background_color)
        self.label = label
        self.visible = visible  # This will tell if button is "on" or "off"

    def draw(self):
        """
        Draw the button with its label on the screen.
        """
        # Draw the box
        super().draw()

        # Draw label in the middle of the box
        font = pygame.font.Font(None, 30)
        text = font.render(self.label, True, BLACK)
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        self.screen.blit(text, text_rect)

    def is_clicked(self, mouse_pos):
        """
        Check if the mouse is over the button.

        :param mouse_pos: mouse position
        :return: True if the button has been clicked, False otherwise
        """
        return super().has_mouse_over(mouse_pos)
    
    def update(self, new_x=None, new_y=None, new_width=None, new_height=None, background_color = None, label = None):
        """
        Update button's attributes.
        """
        if new_x:
            self.x = new_x
        if new_y:
            self.y = new_y
        if new_width:
            self.width = new_width
        if new_height:
            self.height = new_height
        if background_color:
            self.background_color = background_color
        if label:
            self.label = label