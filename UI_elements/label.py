import pygame
from color import BLACK

class Label:
    """
    A simple label.
    """
    def __init__(self, screen, x, y, color=BLACK, text=''):
        self.font = pygame.font.Font('fonts/arial.ttf', 20) 
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
        label_rect.center = (self.x, self.y)
        self.screen.blit(lbl_text, label_rect)