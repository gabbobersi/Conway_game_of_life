import pygame

class Screen:
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
        self._screen = pygame.display.set_mode((self.width, self.height))

    def resize(self, width:int, height:int):
        self.width = width
        self.height = height
        pygame.display.set_mode((self.width, self.height))

    def get_size(self):
        return (self.width, self.height)
    
    def get_screen(self):
        return self._screen
    
    def fill(self, color:tuple[int, int, int]):
        self._screen.fill(color)
