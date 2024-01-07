# src/game.py
import pygame
import random

# Asumiendo que tienes un módulo llamado constantes
from block_factory import (
    BlockFactory,
)  # Asumiendo que tienes un módulo llamado block_factory


class Game:
    def __init__(self, grid):
        """
        Inicializa el juego con un tablero y bloques aleatorios.

        Parameters:
        - grid (Grid): La instancia del tablero.
        """
        self.grid = grid
        self.blocks = BlockFactory.create_blocks()
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

    def get_random_block(self):
        """
        Obtiene un bloque aleatorio de la lista de bloques disponibles.

        Returns:
        - Block: Una instancia de la clase Block.
        """
        if not self.blocks:
            self.blocks = BlockFactory.create_blocks()
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def spawn_next_block(self):
        """
        Genera y asigna el siguiente bloque al juego.
        """
        self.current_block = self.next_block
        self.next_block = self.get_random_block()

    def move(self, delta_x, delta_y):
        """
        Mueve el bloque actual en la dirección especificada.

        Parameters:
        - delta_x (int): Desplazamiento horizontal.
        - delta_y (int): Desplazamiento vertical.
        """
        next_move_x = self.current_block.position_block_x + delta_x
        next_move_y = self.current_block.position_block_y + delta_y
        if not self.check_collision(next_move_x, next_move_y):
            self.current_block.position_block_x = next_move_x
            self.current_block.position_block_y = next_move_y
            self.print_debug_position()

    def move_left(self):
        """Mueve el bloque actual hacia la izquierda."""
        self.move(-1, 0)

    def move_right(self):
        """Mueve el bloque actual hacia la derecha."""
        self.move(1, 0)

    def move_down(self):
        """
        Mueve el bloque actual hacia abajo.
        Si hay colisión en la parte inferior, bloquea el bloque actual y genera uno nuevo.
        """
        self.move(0, 1)
        if self.check_collision_bottom():
            self.lock_block()
            self.spawn_next_block()

    def move_down_hard(self):
        """
        Mueve el bloque actual hacia abajo hasta el fondo.
        Si hay colisión en la parte inferior, bloquea el bloque actual y genera uno nuevo.
        """
        while not self.check_collision_bottom():
            self.move(0, 1)

        self.lock_block()
        self.spawn_next_block()

    def move_up(self):
        """Mueve el bloque actual hacia arriba."""
        self.rotate()

    def check_collision(self, next_move_x, next_move_y):
        """
        Verifica si hay colisión en la posición especificada para el bloque actual.

        Parameters:
        - next_move_x (int): La nueva posición horizontal.
        - next_move_y (int): La nueva posición vertical.

        Returns:
        - bool: True si hay colisión, False de lo contrario.
        """
        for row_index, row in enumerate(self.current_block.shape):
            for col_index, cell in enumerate(row):
                if cell != 0:
                    board_col = next_move_x + col_index
                    board_row = next_move_y + row_index
                    if (
                        board_row >= self.grid.num_rows
                        or board_col < 0
                        or board_col >= self.grid.num_cols
                        or self.grid.grid[board_row][board_col] != 0
                    ):
                        return True
        return False

    def check_collision_bottom(self):
        """
        Verifica si hay colisión en la parte inferior del bloque actual.

        Returns:
        - bool: True si hay colisión en la parte inferior, False de lo contrario.
        """
        delta_x = self.current_block.position_block_x
        delta_y = self.current_block.position_block_y + 1
        return self.check_collision(delta_x, delta_y)

    def lock_block(self):
        """Solidifica el bloque actual en el tablero."""
        for row_index, row in enumerate(self.current_block.shape):
            for col_index, cell in enumerate(row):
                if cell != 0:
                    board_col = self.current_block.position_block_x + col_index
                    board_row = self.current_block.position_block_y + row_index
                    self.grid.grid[board_row][board_col] = self.current_block.id

    def rotate(self):
        """
        Rota la pieza actual en sentido horario.
        """
        # Copia la forma actual de la pieza
        current_shape = self.current_block.shape
        # Calcula la nueva forma después de la rotación (sentido horario)
        new_shape = list(zip(*reversed(current_shape)))

        # Calcula las posiciones después de la rotación
        next_move_x, next_move_y = (
            self.current_block.position_block_x,
            self.current_block.position_block_y,
        )

        # Ajusta la posición si la nueva forma se sale del borde izquierdo o derecho
        next_move_x = max(0, min(next_move_x, self.grid.num_cols - len(new_shape[0])))

        # Verifica si la nueva forma se ajusta dentro de los límites del grid
        if not self.check_collision(next_move_x, next_move_y):
            # Actualiza la forma y la posición de la pieza actual
            self.current_block.shape, self.current_block.position_block_x = (
                new_shape,
                next_move_x,
            )
            self.print_debug_position()

    def print_debug_position(self):
        """Imprime la posición del bloque actual con fines de depuración."""
        print(
            f"Posición de la pieza: ({self.current_block.position_block_x}, {self.current_block.position_block_y})"
        )
