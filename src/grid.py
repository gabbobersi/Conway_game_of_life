import random

import pygame

from UI_elements.color import Color
from team import TeamManager


class Grid:
    def __init__(self, screen: pygame.Surface, cell_size: int, team_manager: TeamManager):
        self.screen = screen
        self.window_width, self.window_height = self.screen.get_size()

        self.cell_size = cell_size
        self.width = self.window_width // self.cell_size
        self.height = (self.window_height) // self.cell_size
        self.grid = [[Color.WHITE.value for _ in range(self.width)] for _ in range(self.height)]

        self.player = team_manager.player
        self.enemy = team_manager.enemy

        self._alive_cells_counter = 0
        self._dead_cells_counter = 0
        self._born_cells_counter = 0

    def apply_game_rules(self):
        new_grid = [[Color.WHITE.value for _ in range(self.width)] for _ in range(self.height)]

        for x in range(self.width):
            for y in range(self.height):
                new_grid = self.modify_cell_by_rule(x, y, self.player.color, new_grid)
                new_grid = self.modify_cell_by_rule(x, y, self.enemy.color, new_grid)

        # Grid update
        for x in range(self.width):
            for y in range(self.height):
                self.grid[y][x] = new_grid[y][x]

    def modify_cell_by_rule(self, x: int, y: int, color: tuple[int, int, int], new_grid: list):
        live_neighbors = self.count_live_neighbors(x, y, color)

        if self.grid[y][x] == color:  # Live cell   
            if live_neighbors < 2 or live_neighbors > 3:
                self._dead_cells_counter += 1
                new_grid[y][x] = Color.WHITE.value  # Dies for underpopulation or overpopulation
            else:
                new_grid[y][x] = color  # Survives to the next generation
                self._alive_cells_counter += 1
        else:  # Dead cell
            if live_neighbors == 3:
                self._born_cells_counter += 1
                new_grid[y][x] = color  # Becomes alive because of reproduction
        return new_grid

    def draw(self):
        self._alive_cells_counter = 0
        self._dead_cells_counter = 0
        self._born_cells_counter = 0

        for x in range(self.width):
            for y in range(self.height):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, self.grid[y][x], rect)

    def clear(self):
        self.grid = [[Color.WHITE.value for _ in range(self.width)] for _ in range(self.height)]
        self.__reset_cells_counter()

    def count_live_neighbors(self, x: int, y: int, color: tuple[int, int, int]):
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
    
    def activate_cell(self, x: int, y: int, color: tuple[int, int, int]):
        if self.grid[y][x] == Color.WHITE.value:
            self.set_color(x, y, color)
        else:
            print("Program is trying to colorate an already activated cells!!!!")

    def deactivate_cell(self, x: int, y: int):
        self.set_color(x, y, Color.WHITE.value)
    
    def get_color(self, x: int, y: int):
        return self.grid[y][x]
    
    def set_color(self, x: int, y: int, color: tuple[int, int, int]):
        self.grid[y][x] = color

    def randomize(self, color:tuple[int, int, int]=None):
        """
        It randomizes the grid.
        """
        if not color:
            color = self.player.color

        for x in range(self.width):
            for y in range(self.height):
                rand = random.randint(0, 4)
                if rand == 0 and self.grid[y][x] == Color.WHITE.value:
                    self.grid[y][x] = color
                elif rand == 1 and self.grid[y][x] not in (self.player.color, self.enemy.color):
                    self.grid[y][x] = Color.WHITE.value

    # def get_alive_cells(self, color):
    #     """
    #     It counts alive cells.
    #     """
    #     count = 0
    #     for x in range(self.width):
    #         for y in range(self.height):
    #             if self.grid[y][x] == color:
    #                 count += 1
    #     return count
    
    def get_alive_cells(self):
        """
        It counts alive cells.
        """
        return self._alive_cells_counter

    def get_born_cells(self):
        """
        It counts born cells.
        """
        return self._born_cells_counter
    
    def get_dead_cells(self):
        """
        It counts dead cells.
        """
        return self._dead_cells_counter
    
    def __reset_cells_counter(self):
        """
        It resets the cells counter.
        """
        self._alive_cells_counter = 0
        self._dead_cells_counter = 0
        self._born_cells_counter = 0
    
    def invasion(self):
        """
        It fills the grid with alive cells of the opposite team.
        """
        self.randomize(self.enemy.color)