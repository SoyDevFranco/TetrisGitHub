# src\block.py
import pygame


class Block:
    def __init__(self, id, name, shape, color, grid, colors):
        self.id = str(id)
        self.name = name
        self.position_block_x = len(grid.grid[0]) // 2
        self.position_block_y = 0
        self.shape = shape
        self.color = color
        self.grid = grid
        self.colors = colors

    def draw_shape(self, screen):
        for row_index, row in enumerate(self.shape):
            for col_index, cell in enumerate(row):
                if cell != 0:
                    x = (
                        self.grid.position_x_grid
                        + (self.position_block_x + col_index) * self.grid.cell_size
                    )
                    y = (
                        self.grid.position_y_grid
                        + (self.position_block_y + row_index) * self.grid.cell_size
                    )

                    pygame.draw.rect(
                        screen,
                        self.color,
                        (
                            x,
                            y,
                            self.grid.cell_size,
                            self.grid.cell_size,
                        ),
                    )
                    pygame.draw.rect(
                        screen,
                        self.colors.LIGHT_BLUE,
                        (x, y, self.grid.cell_size, self.grid.cell_size),
                        1,
                    )
