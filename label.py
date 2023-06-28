import pygame

class Label:
    def __init__(self, screen, text, x, y, color):
        self.font = pygame.font.Font('fonts/arial.ttf', 20) 
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self):
        lbl_text = self.font.render(self.text, True, self.color)
        label_rect = lbl_text.get_rect()
        label_rect.center = (self.x, self.y)
        self.screen.blit(lbl_text, label_rect)