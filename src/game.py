# game.py
import random
from block import Block
from drawBoard import *

colors = Colors()
blocks = [
    Block("I", "Long Bar", [[1, 1, 1, 1]], colors.CYAN),
    Block("O", "Square", [[1, 1], [1, 1]], colors.RED),
    Block("T", "T-Shape", [[0, 1, 0], [1, 1, 1]], colors.PURPLE),
    Block("L", "L-Shape", [[1, 0, 0], [1, 1, 1]], colors.ORANGE),
    Block("S", "S-Shape", [[0, 1, 1], [1, 1, 0]], colors.GREEN),
    Block("Z", "Z-Shape", [[1, 1, 0], [0, 1, 1]], colors.YELLOW),
    Block("J", "J-Shape", [[0, 0, 1], [1, 1, 1]], colors.LAVENDER),
]


class Game:
    def __init__(self, grid):
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.grid = grid

    def get_random_block(self):
        return random.choice(blocks)

    def move_left(self):
        print(
            f"Before Move Left: ({self.current_block.column_offset}, {self.current_block.row_offset})"
        )
        self.move(-1, 0)

    def move_right(self):
        print(
            f"Before Move Right: ({self.current_block.column_offset}, {self.current_block.row_offset})"
        )
        self.move(1, 0)

    def move_down(self):
        print(
            f"Before Move Down: ({self.current_block.column_offset}, {self.current_block.row_offset})"
        )
        self.move(0, 1)

    def move(self, dx, dy):
        next_move_x = self.current_block.column_offset + dx
        next_move_y = self.current_block.row_offset + dy

        if not self.check_collision(next_move_x, next_move_y):
            self.current_block.column_offset = next_move_x
            self.current_block.row_offset = next_move_y
            print(f"Current Position: ({next_move_x}, {next_move_y})")
        else:
            print(f"Collision detected! Cannot move to ({next_move_x}, {next_move_y}).")

    def check_collision(self, next_move_x, next_move_y):
        for row_index, row in enumerate(self.current_block.shape):
            for col_index, cell in enumerate(row):
                if cell != 0:
                    board_col = next_move_x + col_index
                    board_row = next_move_y + row_index

                    if not (
                        0 <= board_row < len(self.grid.grid)
                        and 0 <= board_col < len(self.grid.grid[0])
                    ):
                        print(
                            f"Out of bounds! Cannot move to ({next_move_x}, {next_move_y})."
                        )
                        return True

                    if self.grid.grid[board_row][board_col] != 0:
                        print(
                            f"Collision detected at ({board_col}, {board_row}). Cannot move to ({next_move_x}, {next_move_y})."
                        )
                        return True

        return False
