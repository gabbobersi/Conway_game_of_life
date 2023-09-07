import pygame

class Screen:
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
        self.__screen = pygame.display.set_mode((self.width, self.height))

    def resize(self, width:int, height:int):
        self.width = width
        self.height = height
        pygame.display.set_mode((self.width, self.height))

    def get_size(self):
        return (self.width, self.height)
    
    def get_screen(self):
        return self.__screen
    
    def fill(self, color:tuple[int, int, int]):
        self.__screen.fill(color)
