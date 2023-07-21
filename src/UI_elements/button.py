import pygame
from UI_elements.color import *
from UI_elements.box import Box
from UI_elements.label import Label

class Button(Box):
    """
    A simple box with a labels on it. It can be clicked.
    """
    def __init__(self, screen, text = '', visible = False, x=None, y=None, width=100, height=50, background_color=CUSTOM_RED):
        super().__init__(screen, x, y, width, height, background_color)
        self.label = Label(screen, x + 15, y + 15, text)
        self.visible = visible  # This will tell if button is "on" or "off"
        self.text = text

    def draw(self):
        """
        Draw the button with its label on the screen.
        """
        # Draw the box
        super().draw()
        self.label.draw(self.text)
        # # Draw label in the middle of the box
        # font = pygame.font.Font(None, 30)
        # text = font.render(self.label, True, BLACK)
        # text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        # self.screen.blit(text, text_rect)

    def is_clicked(self, mouse_pos):
        """
        Check if the mouse is over the button.

        :param mouse_pos: mouse position
        :return: True if the button has been clicked, False otherwise
        """
        if super().has_mouse_over(mouse_pos):
            print("{} button clicked".format(self.text))
            return True
        return False
    
    def update(self, new_x=None, new_y=None, new_width=None, new_height=None, background_color = None, text = None):
        """
        Update button's attributes.
        """
        super().update(new_x, new_y, new_width, new_height, background_color)
        if text:
            self.text = text
        self.label.update(new_x = self.x + 15, new_y = self.y + 15)
