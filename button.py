import pygame

from costants import WINDOW_WIDTH, WINDOW_HEIGHT
from color import *

class Button:
    def __init__(self, screen, label = '', visible = False, x=None, y=None):
        self.screen = screen
        self.width = button_width = 100
        self.height = button_height = 50
        
        if not x:
            self.x = (WINDOW_WIDTH - button_width) // 2
        else:
            self.x = x

        if not y:
            self.y = (WINDOW_HEIGHT - button_height) // 2
        else:
            self.y = y

        self.label = label
        self.visible = visible  # This will tell if button is "on" or "off"

    def draw(self):
        """
        Draw the button with its label on the screen.
        """
        # Draw button
        button_color = CUSTOM_RED
        settings = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, button_color, settings, 0)
        pygame.draw.rect(self.screen, BLACK, settings, 2)

        # Draw label in the middle of the button
        font = pygame.font.Font(None, 30)
        text = font.render(self.label, True, BLACK)
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        self.screen.blit(text, text_rect)

    def is_clicked(self, mouse_pos):
        """
        Check if the button has been clicked.

        :param mouse_pos: mouse position
        :return: True if the button has been clicked, False otherwise
        """
        if self.x <= mouse_pos[0] <= self.x + self.width:           # Mouse is between the left and right side of the button
            if self.y <= mouse_pos[1] <= self.y + self.height:      # Mouse is between the top and bottom side of the button
                return True
        return False