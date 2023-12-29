# drawBoard.py
from constantes import *
import pygame

colors = Colors()


class Grid:
    def __init__(self):
        self.col = 10
        self.row = 20
        self.cell_size = 30
        self.center_x = (WIDTH - (self.cell_size * self.col)) // 3.5
        self.center_y = (HEIGHT - (self.cell_size * self.row)) // 2
        self.grid = [[0] * self.col for _ in range(self.row)]

    def draw_board(self, screen):
        """Dibuja el tablero en la pantalla."""
        for row in range(BOARD_HEIGHT):
            for col in range(BOARD_WIDTH):
                x, y = (self.center_x + col * self.cell_size), (
                    self.center_y + row * self.cell_size
                )
                cell_value = self.grid[row][col]
                color = colors.DARK_GREY if cell_value == 0 else cell_value

                pygame.draw.rect(screen, color, (x, y, self.cell_size, self.cell_size))
                pygame.draw.rect(
                    screen,
                    colors.LIGHT_BLUE,
                    (x, y, self.cell_size, self.cell_size),
                    1,
                )
