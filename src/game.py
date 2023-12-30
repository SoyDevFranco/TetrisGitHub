# game.py
import random
from block import Block
from constantes import *

colors = Colors()


class Game:
    def __init__(self):
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

    blocks = [
        Block("I", "Long Bar", [[1, 1, 1, 1]], colors.CYAN),
        Block("O", "Square", [[1, 1], [1, 1]], colors.RED),
        Block("T", "T-Shape", [[0, 1, 0], [1, 1, 1]], colors.PURPLE),
        Block("L", "L-Shape", [[1, 0, 0], [1, 1, 1]], colors.ORANGE),
        Block("S", "S-Shape", [[0, 1, 1], [1, 1, 0]], colors.GREEN),
        Block("Z", "Z-Shape", [[1, 1, 0], [0, 1, 1]], colors.YELLOW),
        Block("J", "J-Shape", [[0, 0, 1], [1, 1, 1]], colors.LAVENDER),
    ]

    def get_current_block(self):
        return self.current_block

    def get_random_block(self):
        return random.choice(self.blocks)
