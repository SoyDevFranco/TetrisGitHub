# src/block.py

import pygame
from drawBoard import Grid
from constantes import Colors
from box import Box


class Block:
    def __init__(self, id, name, shape):
        """
        Inicializa un objeto Block.

        Parámetros:
        - id: Identificador único del bloque.
        - name: Nombre del bloque.
        - shape: Forma del bloque representada como una matriz de 0 y 1.
        """
        self.id = int(id)
        self.name = name
        self.shape = shape
        self.cell_size = 30

        # Crea una instancia de Grid para gestionar las posiciones en el tablero
        self.grid = Grid()
        self.colors = Colors.get_cell_colors()

        # Calcula la posición inicial del bloque en función del tamaño de la forma
        self.position_block_x = (self.grid.num_cols // 2) - (len(shape[0]) // 2)
        self.position_block_y = 0

    def draw_shape(self, screen):
        """
        Dibuja la forma del bloque en la pantalla.

        Parámetros:
        - screen: Superficie de la pantalla donde se dibujará el bloque.
        """
        for row_index, row in enumerate(self.shape):
            for col_index, cell in enumerate(row):
                if cell != 0:
                    cell_rect = pygame.Rect(
                        (self.position_block_x + col_index) * self.cell_size
                        + self.grid.grid_position_x,
                        (self.position_block_y + row_index) * self.cell_size
                        + self.grid.grid_position_y,
                        self.cell_size,
                        self.cell_size,
                    )

                    # Dibuja un rectángulo sólido y otro bordeado alrededor de la celda
                    pygame.draw.rect(screen, self.colors[self.id], cell_rect)
                    pygame.draw.rect(screen, Colors.light_blue, cell_rect, 1)

    def draw_shape_preview(self, screen, box):
        """
        Dibuja la forma del bloque en la pantalla, centrada en una caja específica.

        Parámetros:
        - screen: Superficie de la pantalla donde se dibujará el bloque.
        - box: Instancia de la clase Box que representa la caja específica.
        """
        box_center_x, box_center_y = box.get_center()

        for row_index, row in enumerate(self.shape):
            for col_index, cell in enumerate(row):
                if cell != 0:
                    cell_rect = pygame.Rect(
                        col_index * self.cell_size
                        + box_center_x
                        - (len(self.shape[0]) * self.cell_size) // 2,
                        row_index * self.cell_size
                        + box_center_y
                        - (len(self.shape) * self.cell_size) // 2,
                        self.cell_size,
                        self.cell_size,
                    )

                    # Dibuja un rectángulo sólido y otro bordeado alrededor de la celda
                    pygame.draw.rect(screen, self.colors[self.id], cell_rect)
                    pygame.draw.rect(screen, Colors.light_blue, cell_rect, 1)
