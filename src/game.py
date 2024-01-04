# src/game.py
import random

from constantes import *
from block_factory import BlockFactory


class Game:
    def __init__(self, Grid):
        self.grid = Grid
        self.colors = Colors()
        self.blocks = BlockFactory.create_blocks()
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

    def get_random_block(self):
        return random.choice(self.blocks)

    def spawn_next_block(self):
        """Genera y asigna la siguiente pieza."""

        self.current_block = self.next_block
        self.next_block = self.get_random_block()

    def move(self, dx, dy):
        next_move_x = self.current_block.position_block_x + dx
        next_move_y = self.current_block.position_block_y + dy
        if not self.check_collision_bottom():
            self.current_block.position_block_x = next_move_x
            self.current_block.position_block_y = next_move_y

        # Agrega impresión para depurar
        print(f"Posición de la pieza: ({next_move_x}, {next_move_y})")

    def move_left(self):
        self.move(-1, 0)

    def move_right(self):
        self.move(1, 0)

    def move_up(self):
        self.rotate()

    def move_down(self):
        self.move(0, 1)
        if self.check_collision_bottom():
            self.fix_block()
            self.spawn_next_block()  # Agrega esta línea para generar un nuevo bloque

    def check_collision_bottom(self):
        for row_index, row in enumerate(self.current_block.shape):
            for col_index, cell in enumerate(row):
                if cell != 0:
                    board_col = self.current_block.position_block_x + col_index
                    board_row = (
                        self.current_block.position_block_y
                        + self.current_block.center_block[1]
                    ) + row_index

                    if (
                        board_row >= self.grid.num_rows
                        or self.grid.board[board_row][board_col] != 0
                    ):
                        print(f"Colisión con bordes en: ({board_col}, {board_row})")
                        return True
        return False

    def fix_block(self):
        """Solidifica la pieza actual en el tablero."""
        for row_index, row in enumerate(self.current_block.shape):
            for col_index, cell in enumerate(row):
                if cell != 0:
                    board_col = self.current_block.position_block_x + col_index
                    board_row = self.current_block.position_block_y + row_index

                    # Corregir: Utiliza el color de la celda de la pieza en el tablero
                    self.grid.board[board_row][board_col] = self.current_block.color
