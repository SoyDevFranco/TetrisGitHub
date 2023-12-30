from constantes import Colors
import pygame
from constantes import *

colors = Colors()


class Block:
    def __init__(self, id, name, shape, color):
        self.id = str(id)
        self.name = name
        self.grid_x, self.grid_y = 4, 0  # Coordenadas en la cuadrícula
        self.shape = shape
        self.color = color
        self.cell_size = 30

    def draw_shape(self, screen, grid):
        for row_offset, row in enumerate(self.shape):
            for col_offset, cell in enumerate(row):
                if cell == 1:
                    board_col = self.grid_x + col_offset
                    board_row = self.grid_y + row_offset

                    # Calcular las coordenadas en píxeles en la pantalla
                    x = grid.center_x + board_col * grid.cell_size
                    y = grid.center_y + board_row * grid.cell_size

                    pygame.draw.rect(
                        screen,
                        self.color,
                        (x, y, self.cell_size, self.cell_size),
                    )
                    pygame.draw.rect(
                        screen,
                        colors.LIGHT_BLUE,
                        (x, y, self.cell_size, self.cell_size),
                        1,
                    )


# Definición de los bloques
I_BLOCK = Block("I", "Long Bar", [[1, 1, 1, 1]], colors.CYAN)
O_BLOCK = Block("O", "Square", [[1, 1], [1, 1]], colors.RED)
T_BLOCK = Block("T", "T-Shape", [[0, 1, 0], [1, 1, 1]], colors.PURPLE)
L_BLOCK = Block("L", "L-Shape", [[1, 0, 0], [1, 1, 1]], colors.ORANGE)
S_BLOCK = Block("S", "S-Shape", [[0, 1, 1], [1, 1, 0]], colors.GREEN)
Z_BLOCK = Block("Z", "Z-Shape", [[1, 1, 0], [0, 1, 1]], colors.YELLOW)
J_BLOCK = Block("J", "J-Shape", [[0, 0, 1], [1, 1, 1]], colors.LAVENDER)

# ejemplo
# class IBlock(Block):
#     def __init__(self):
#         super().__init__()
#         self.id = "I"
#         self.name = "Long Bar"
#         self.shape = [[1, 1, 1, 1]]
#         self.colors = colors.CYAN
