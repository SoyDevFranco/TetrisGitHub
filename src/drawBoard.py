import pygame
from constantes import *


class Grid:
    def __init__(self, colors):
        self.col = 10
        self.row = 20
        self.cell_size = 30
        self.position_x_grid = (WIDTH - (self.cell_size * self.col)) // 3.5
        self.position_y_grid = (HEIGHT - (self.cell_size * self.row)) // 2
        self.grid = [[0] * self.col for _ in range(self.row)]
        self.colors = colors

    def draw_board(self, screen):
        """Dibuja el tablero en la pantalla."""
        for row in range(self.row):
            for col in range(self.col):
                x, y = (self.position_x_grid + col * self.cell_size), (
                    self.position_y_grid + row * self.cell_size
                )
                cell_value = self.grid[row][col]
                color = self.colors.DARK_GREY if cell_value == 0 else cell_value

                pygame.draw.rect(screen, color, (x, y, self.cell_size, self.cell_size))
                pygame.draw.rect(
                    screen,
                    self.colors.LIGHT_BLUE,
                    (x, y, self.cell_size, self.cell_size),
                    1,
                )

                # Imprime las coordenadas de la celda
                # print(f"Celda en ({row}, {col}): x={x}, y={y}")


# Resto del código...
