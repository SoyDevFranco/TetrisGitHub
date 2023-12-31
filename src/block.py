import pygame
from constantes import *


class Block:
    def __init__(self, id, name, shape, color):
        self.id = str(id)
        self.name = name
        self.row_offset = 0
        self.column_offset = 0
        self.shape = shape
        self.color = color

    def draw_shape(self, screen, grid, colors):
        center_grid_x = grid.position_x_grid + (grid.col * grid.cell_size) // 2

        for row_index, row in enumerate(self.shape):
            for col_index, cell in enumerate(row):
                if cell != 0:
                    center_block_x = col_index - (len(self.shape[0]) // 2)
                    x = center_grid_x + (
                        (self.column_offset + center_block_x) * grid.cell_size
                    )

                    y = (
                        grid.position_y_grid
                        + (self.row_offset + row_index) * grid.cell_size
                    )

                    pygame.draw.rect(
                        screen,
                        self.color,
                        (x, y, grid.cell_size, grid.cell_size),
                    )
                    pygame.draw.rect(
                        screen,
                        colors.LIGHT_BLUE,
                        (x, y, grid.cell_size, grid.cell_size),
                        1,
                    )
