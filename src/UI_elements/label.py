from typing import Callable

import pygame

from UI_elements.base_classes.entity import Entity
from UI_elements.color import Color

class Label(Entity):
    """
    A simple label.
    """
    def __init__(self, screen:pygame.Surface, x:int=20, y:int=20, text:str='', color:tuple[int, int, int]=Color.BLACK.value):
        super().__init__(x, y)
        self.screen = screen
        self.font = pygame.font.Font('fonts/Gameplay.ttf', 14) 
        self.text = text
        self.color = color
    
    def draw(self, custom_text:str=''):
        if custom_text:
            self.text = custom_text
        text = self.font.render(self.text, True, self.color)
        rect = text.get_rect()
        rect.topleft = (self.x, self.y)
        self.screen.blit(text, rect)

    def update(self, new_x:int=None, new_y:int=None, new_text:str=None, new_color:tuple[int, int, int]=None):
        """
        Update label's attributes.
        """
        if new_x:
            self.x = new_x
        if new_y:
            self.y = new_y
        if new_color:
            self.color = new_color
        if new_text:
            self.text = new_text


class TemplateLabel(Label):
    """
    A label whose text is generated via template.
    """
    def __init__(self, screen:pygame.Surface, x:int, y:int, template_text:str, template_method:Callable, color:tuple[int, int, int]=Color.BLACK.value):
        super().__init__(screen, x, y, '', color=color)
        self.template_text = template_text      # Example: "Score: {}"
        self.template_method = template_method  # Method that returns the value to be inserted in the template
    
    def draw(self):
        value = self.template_method()
        super().draw(self.template_text.format(value))


class InteractiveLabel(Label):
    """
    A label that can be clicked.
    """
    def __init__(self, screen:pygame.Surface, x:int, y:int, width:int, height:int, text:str=''):
        super().__init__(screen, x, y, text)
        self.width = width
        self.height = height

    def is_clicked(self, event:pygame.event.Event, mouse_pos:tuple[int, int, int]):
        """
        Check if the mouse is over the button, during a MOUSEBUTTONDOWN event.

        :param mouse_pos: mouse position
        :param event: event to check
        :return: True if the button has been clicked, False otherwise
        """
        if event.type != pygame.MOUSEBUTTONDOWN:
            raise ValueError("Error :: Invalid event type {}. MOUSEBUTTON expected.".format(event))
        return super().has_mouse_over(mouse_pos)
    