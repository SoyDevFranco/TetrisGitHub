# src/drawBoard.py
import pygame
from constantes import Colors, Constans

colors = Colors()
constants = Constans()


class Grid:
    def __init__(self):
        self.col = 10
        self.row = 20
        self.cell_size = 30
        self.position_x_grid = (constants.WIDTH - (self.cell_size * self.col)) // 3.5
        self.position_y_grid = (constants.HEIGHT - (self.cell_size * self.row)) // 2
        self.grid = [[0] * self.col for _ in range(self.row)]

    def draw_board(self, screen):
        """Dibuja el tablero en la pantalla."""
        for row in range(self.row):
            for col in range(self.col):
                x, y = (
                    self.position_x_grid + col * self.cell_size,
                    self.position_y_grid + row * self.cell_size,
                )
                cell_value = self.grid[row][col]
                color = cell_value if cell_value != 0 else colors.DARK_GREY

                pygame.draw.rect(screen, color, (x, y, self.cell_size, self.cell_size))
                pygame.draw.rect(
                    screen,
                    colors.LIGHT_BLUE,
                    (x, y, self.cell_size, self.cell_size),
                    1,
                )

        print(f"Celda ({row}, {col}): Valor = {cell_value}, Color = {color}")

        print("Estado del tablero después de dibujar:")
        for row in self.grid:
            print(row)
        print("\n")
