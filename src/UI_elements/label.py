import pygame

from UI_elements.color import BLACK

class Label:
    """
    A simple label.
    """
    def __init__(self, screen, x=20, y=20, text='', color=BLACK):
        self.font = pygame.font.Font('fonts/Gameplay.ttf', 14) 
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self, custom_text=''):
        if custom_text:
            self.text = custom_text
        text = self.font.render(self.text, True, self.color)
        rect = text.get_rect()
        rect.topleft = (self.x, self.y)
        self.screen.blit(text, rect)

    def update(self, new_x=None, new_y=None, new_text=None, new_color=None):
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
    def __init__(self, screen, x, y, template_text, template_method, color=BLACK):
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
    def __init__(self, screen, x, y, width, height, text=''):
        super().__init__(screen, x, y, text)
        self.width = width
        self.height = height

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
    