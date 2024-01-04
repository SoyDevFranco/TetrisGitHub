# src\block.py
import pygame
from drawBoard import Grid
from constantes import Colors


class Block:
    def __init__(self, id, shape, color):
        self.id = str(id)
        self.shape = shape
        self.color = color
        self.cell_size = 30

        # Mueve la creación de la instancia de Grid aquí
        self.grid = Grid()
        self.colors = Colors()

        # Ahora puedes usar self.grid.num_cols
        self.position_block_x = self.grid.num_cols // 2
        self.position_block_y = 0
        self.center_block = (
            len(shape) // 2,  # Fila central
            len(shape[0]) // 2,  # Columna central
        )

    def draw_shape(self, screen):
        for row_index, row in enumerate(self.shape):
            for col_index, cell in enumerate(row):
                if cell != 0:
                    x = (
                        self.grid.grid_position_x
                        + (self.position_block_x + col_index) * self.cell_size
                    )
                    y = (
                        self.grid.grid_position_y
                        + (self.position_block_y + row_index) * self.cell_size
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
