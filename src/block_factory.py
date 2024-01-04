# src/block_factory.py
from block import Block
from constantes import Colors


class BlockFactory:
    @staticmethod
    def create_blocks():
        colors = Colors()
        blocks = [
            Block("I", [[1, 1, 1, 1]], colors.CYAN),
            Block("O", [[1, 1], [1, 1]], colors.RED),
            Block("T", [[0, 1, 0], [1, 1, 1]], colors.PURPLE),
            Block("L", [[1, 0, 0], [1, 1, 1]], colors.ORANGE),
            Block("S", [[0, 1, 1], [1, 1, 0]], colors.GREEN),
            Block("Z", [[1, 1, 0], [0, 1, 1]], colors.YELLOW),
            Block("J", [[0, 0, 1], [1, 1, 1]], colors.LAVENDER),
        ]
        return blocks
