import pygame

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
TITLE = pygame.display.set_caption('Game of Life')

CELL_SIZE = 10

GRID_WIDTH = WINDOW_WIDTH // CELL_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // CELL_SIZE

CLOCK = pygame.time.Clock()
