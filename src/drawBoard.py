import pygame
from constantes import Colors, Constants


class Grid:
    def __init__(self):
        self.num_cols = 10
        self.num_rows = 20
        self.cell_size = 30
        self.constants = Constants()
        self.colors = Colors()
        self.grid_position_x = self.calculate_grid_position_x()
        self.grid_position_y = self.calculate_grid_position_y()
        self.grid = [[0] * self.num_cols for _ in range(self.num_rows)]

    def calculate_grid_position_x(self):
        return (self.constants.WIDTH - (self.cell_size * self.num_cols)) // 3.5

    def calculate_grid_position_y(self):
        return (self.constants.HEIGHT - (self.cell_size * self.num_rows)) // 2

    def draw_board(self, screen):
        """Dibuja el tablero en la pantalla."""
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                x, y = (
                    self.grid_position_x + col * self.cell_size,
                    self.grid_position_y + row * self.cell_size,
                )
                cell_value = self.grid[row][col]
                color = cell_value if cell_value != 0 else self.colors.DARK_GREY

                pygame.draw.rect(screen, color, (x, y, self.cell_size, self.cell_size))
                pygame.draw.rect(
                    screen,
                    self.colors.LIGHT_BLUE,
                    (x, y, self.cell_size, self.cell_size),
                    1,
                )
