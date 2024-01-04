# src/game.py
import random
from drawBoard import Grid
from constantes import *
from block_factory import BlockFactory


class Game:
    def __init__(self):
        self.grid = Grid()
        self.colors = Colors()
        self.blocks = BlockFactory.create_blocks()
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

    def get_random_block(self):
        return random.choice(self.blocks)

    def move(self, dx, dy):
        next_move_x = self.current_block.position_block_x + dx
        next_move_y = self.current_block.position_block_y + dy

        if not self.check_collision_borders(next_move_x, next_move_y):
            self.current_block.position_block_x = next_move_x
            self.current_block.position_block_y = next_move_y

            # Agrega impresión para depurar
            print(f"Posición de la pieza: ({next_move_x}, {next_move_y})")

    def move_left(self):
        self.move(-1, 0)

    def move_right(self):
        self.move(1, 0)

    def move_down(self):
        self.move(0, 1)
        if self.check_collision_borders(
            self.current_block.position_block_x,
            self.current_block.position_block_y,
        ):
            self.fix_block()

    def check_collision_borders(self, next_move_x, next_move_y):
        for row_index, row in enumerate(self.current_block.shape):
            for col_index, cell in enumerate(row):
                if cell != 0:
                    board_col = next_move_x + col_index
                    board_row = next_move_y + row_index

                    # Verificar si el bloque está dentro del rango del tablero
                    if (
                        board_row >= self.grid.num_rows  # Modificado a >=
                        or board_col < 0
                        or board_col >= self.grid.num_cols
                    ):
                        # Depuración
                        print(f"Colisión con bordes en: ({board_col}, {board_row})")

                        return True

        return False

    def fix_block(self):
        """Solidifica la pieza actual en el tablero."""
        for row_index, row in enumerate(self.current_block.shape):
            for col_index, cell in enumerate(row):
                if cell != 0:
                    block_col = self.current_block.position_block_x + col_index
                    block_row = self.current_block.position_block_y + row_index

                    # Verifica si la posición está dentro del rango del tablero
                    if (
                        0 <= block_row < self.grid.num_rows
                        and 0 <= block_col < self.grid.num_cols
                    ):
                        # Actualiza el color en el tablero
                        self.grid.grid[block_row][block_col] = self.current_block.color
