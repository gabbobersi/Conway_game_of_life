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

    def is_clicked(self, event, mouse_pos):
        """
        Check if the mouse is over the button, during a MOUSEBUTTONDOWN event.

        :param mouse_pos: mouse position
        :param event: event to check
        :return: True if the button has been clicked, False otherwise
        """
        if event.type != pygame.MOUSEBUTTONDOWN:
            raise ValueError("Error :: Invalid event type {}. MOUSEBUTTON expected.".format(event))
        return super().has_mouse_over(mouse_pos)