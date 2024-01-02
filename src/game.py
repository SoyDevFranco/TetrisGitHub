# src\game.py
import random
from block import Block
from drawBoard import Grid
from constantes import Colors

colors = Colors()
grid = Grid()


class Game:
    def __init__(self):
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.grid = grid

    def get_random_block(self):
        return random.choice(
            [
                Block("I", "Long Bar", [[1, 1, 1, 1]], colors.CYAN),
                Block("O", "Square", [[1, 1], [1, 1]], colors.RED),
                Block("T", "T-Shape", [[0, 1, 0], [1, 1, 1]], colors.PURPLE),
                Block("L", "L-Shape", [[1, 0, 0], [1, 1, 1]], colors.ORANGE),
                Block("S", "S-Shape", [[0, 1, 1], [1, 1, 0]], colors.GREEN),
                Block("Z", "Z-Shape", [[1, 1, 0], [0, 1, 1]], colors.YELLOW),
                Block("J", "J-Shape", [[0, 0, 1], [1, 1, 1]], colors.LAVENDER),
            ]
        )

    def move(self, dx, dy):
        next_move_x = self.current_block.position_block_x + dx
        next_move_y = self.current_block.position_block_y + dy

        if not self.check_collision(next_move_x, next_move_y):
            self.current_block.position_block_x = next_move_x
            self.current_block.position_block_y = next_move_y

    def move_left(self):
        self.move(-1, 0)

    def move_right(self):
        self.move(1, 0)

    def move_down(self):
        self.move(0, 1)

    def check_collision(self, next_move_x, next_move_y):
        for row_index, row in enumerate(self.current_block.shape):
            for col_index, cell in enumerate(row):
                if cell != 0:
                    board_col = next_move_x + col_index
                    board_row = next_move_y + row_index

                    # Verificar si está fuera del rango antes de acceder
                    if (
                        board_col < 0
                        or board_col >= self.grid.col
                        or board_row >= self.grid.row
                    ):
                        return True

                    # Asegúrate de que board_row no sea negativo
                    if board_row != 0:
                        cell_value = grid.grid[board_row][board_col]
                        if cell_value != 0:
                            return True
        return False  # No hay colisiones

    def solidify_block(self):
        """Solidifica la pieza actual en el tablero."""
        for row_index, row in enumerate(self.current_block.shape):
            for col_index, cell in enumerate(row):
                if cell != 0:
                    block_col = self.current_block.position_block_x + col_index
                    block_row = self.current_block.position_block_y + row_index
                    print(f"Solidificando celda en ({block_row}, {block_col})")
                    print(f"Color de la pieza: {self.current_block.color}")
                    print("Estado del tablero antes de la asignación:", self.grid)
                    self.grid.grid[block_row][block_col] = self.current_block.color
                    print("Estado del tablero después de la asignación:", self.grid)
