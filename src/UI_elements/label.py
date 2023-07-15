import pygame

from UI_elements.color import BLACK

class Label:
    """
    A simple label.
    """
    def __init__(self, screen, x, y, color=BLACK, text=''):
        self.font = pygame.font.Font('fonts/Gameplay.ttf', 14) 
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self, custom_text=''):
        if custom_text:
            self.text = custom_text
        lbl_text = self.font.render(self.text, True, self.color)
        label_rect = lbl_text.get_rect()
        label_rect.topleft = (self.x, self.y)
        self.screen.blit(lbl_text, label_rect)

class InteractiveLabel(Label):
    def __init__(self, screen, x, y, width, height, text=''):
        super().__init__(screen, x, y, width, height, text)

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
    