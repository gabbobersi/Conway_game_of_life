import pygame

from UI_elements.color import Color
from UI_elements.box import Box
from UI_elements.label import Label

class Button(Box):
    """
    A simple box with a labels on it. It can be clicked.
    """
    def __init__(
            self, screen:pygame.Surface, text:str = '', visible:bool = False, x:int=None, y:int=None, 
            width:int=100, height:int=50, background_color:tuple[int, int, int]=Color.CUSTOM_RED.value
            ):
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

    def is_clicked(self, mouse_pos:tuple[int, int, int]):
        """
        Check if the mouse is over the button.

        :param mouse_pos: mouse position
        :return: True if the button has been clicked, False otherwise
        """
        return super().has_mouse_over(mouse_pos)
    
    def update(self, new_x:int=None, new_y:int=None, new_width:int=None, new_height:int=None, new_background_color:tuple[int, int, int]= None, text:str = None):
        """
        Update button's attributes.
        """
        super().update(new_x, new_y, new_width, new_height, new_background_color)
        if text:
            self.text = text
        self.label.update(new_x = self.x + 15, new_y = self.y + 15) # Updating label position according to button position
