import random

import pygame
from color import *

class Grid:
    def __init__(self, screen, cell_size):
        self.screen = screen
        self.window_width, self.window_height = self.screen.get_size()

        self.cell_size = cell_size
        self.width = self.window_width // self.cell_size
        self.height = self.window_height // self.cell_size
        self.grid = [[WHITE for _ in range(self.width)] for _ in range(self.height)]
        
        self.killed_cells_counter = 0
        self.born_cells_counter = 0
        
    @property
    def alive_cells_counter(self):
        return self.get_alive_cells()

    def apply_game_rules(self, player_team):
        new_grid = [[WHITE for _ in range(self.width)] for _ in range(self.height)]
        self.killed_cells_counter = 0
        self.born_cells_counter = 0

        for x in range(self.width):
            for y in range(self.height):
                new_grid = self.modify_cell_by_rule(x, y, player_team.color, new_grid)
                new_grid = self.modify_cell_by_rule(x, y, player_team.get_opposite_team(), new_grid)

        # Grid update
        for x in range(self.width):
            for y in range(self.height):
                self.grid[y][x] = new_grid[y][x]

    def modify_cell_by_rule(self, x, y, color, new_grid):
        live_neighbors = self.count_live_neighbors(x, y, color)

        if self.grid[y][x] == color:  # Live cell
            if live_neighbors < 2 or live_neighbors > 3:
                self.killed_cells_counter += 1
                new_grid[y][x] = WHITE  # Dies for underpopulation or overpopulation
            else:
                new_grid[y][x] = color  # Survives to the next generation
        
        else:  # Dead cell
            if live_neighbors == 3:
                self.born_cells_counter += 1
                new_grid[y][x] = color  # Becomes alive because of reproduction
        return new_grid

    def draw(self):
        for x in range(self.width):
            for y in range(self.height):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, self.grid[y][x], rect)

    def clear(self):
        self.grid = [[WHITE for _ in range(self.width)] for _ in range(self.height)]

    def count_live_neighbors(self, x, y, color=RED):
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
                if 0 <= neighbor_x < self.width and 0 <= neighbor_y < self.height:
                    if self.grid[neighbor_y][neighbor_x] == color:
                        count += 1
        return count
    
    def activate_cell(self, x, y, color=RED):
        self.set_color(color, x, y)

    def deactivate_cell(self, x, y):
        self.set_color(WHITE, x, y)
    
    def get_color(self, x, y):
        return self.grid[y][x]
    
    def set_color(self, color, x, y):
        self.grid[y][x] = color

    def randomize(self, color=RED):
        """
        It randomizes the grid.
        """
        for x in range(self.width):
            for y in range(self.height):
                rand = random.randint(0, 4)
                if rand == 0 and self.grid[y][x] == WHITE:
                    self.grid[y][x] = color
                elif rand == 1 and self.grid[y][x] not in (RED, BLUE):
                    self.grid[y][x] = WHITE
                # self.grid[y][x] = RED if random.randint(0, 3) == 0 else WHITE

    def get_alive_cells(self, color=RED):
        """
        It counts alive cells.
        """
        count = 0
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[y][x] == color:
                    count += 1
        return count
    
    def get_dead_cells(self):
        """
        It counts dead cells.
        """
        return self.dead_cells_counter
    
    def invasion(self):
        """
        It fills the grid with alive cells of the opposite team.
        """
        self.randomize(BLUE)