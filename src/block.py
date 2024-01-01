import pygame
from constantes import *
from drawBoard import *

colors = Colors()
grid = Grid(colors)


class Block:
    def __init__(self, id, name, shape, color):
        self.id = str(id)
        self.name = name
        self.position_block_x = len(grid.grid[0]) // 2
        self.position_block_y = 0
        self.shape = shape
        self.color = color

    def draw_shape(self, screen, grid, colors):
        for row_index, row in enumerate(self.shape):
            for col_index, cell in enumerate(row):
                if cell != 0:
                    x = (
                        grid.position_x_grid
                        + (self.position_block_x + col_index) * grid.cell_size
                    )
                    y = (
                        grid.position_y_grid
                        + (self.position_block_y + row_index) * grid.cell_size
                    )

                    pygame.draw.rect(
                        screen,
                        self.color,
                        (
                            x,
                            y,
                            grid.cell_size,
                            grid.cell_size,
                        ),
                    )
                    pygame.draw.rect(
                        screen,
                        colors.LIGHT_BLUE,
                        (x, y, grid.cell_size, grid.cell_size),
                        1,
                    )
