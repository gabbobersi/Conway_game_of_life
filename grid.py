import pygame

from color import WHITE, RED, GREEN
from costants import GRID_WIDTH, GRID_HEIGHT, CELL_SIZE, SCREEN

class Grid:
    def __init__(self):
        self.screen = SCREEN
        self.grid = [[WHITE for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    def apply_game_rules(self):
        new_grid = [[WHITE for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                live_neighbors = self.count_live_neighbors(x, y)

                if self.grid[y][x] == RED:  # Live cell
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[y][x] = WHITE  # Dies for underpopulation or overpopulation
                    else:
                        new_grid[y][x] = RED  # Survives to the next generation
                else:  # Cella morta
                    if live_neighbors == 3:
                        new_grid[y][x] = GREEN  # Becomes alive because of reproduction

        # Grid update
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                self.grid[y][x] = new_grid[y][x]

    def draw(self):
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, self.grid[y][x], rect)

    def count_live_neighbors(self, x, y):
        """
        It counts "live" neighbors of a cell.
        """
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:  # Ignore the cell itself
                    continue

                neighbor_x = x + i
                neighbor_y = y + j

                # Check if the cell is inside the grid
                if 0 <= neighbor_x < GRID_WIDTH and 0 <= neighbor_y < GRID_HEIGHT:
                    if self.grid[neighbor_y][neighbor_x] == RED:
                        count += 1
        return count
    
    def get_color(self, x, y):
        return self.grid[y][x]
    
    def set_color(self, color, x, y):
        self.grid[y][x] = color
