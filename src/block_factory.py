# src/block_factory.py
from block import Block


class BlockFactory:
    @staticmethod
    def create_blocks():
        """
        Crea y devuelve una lista de objetos Block representando diferentes formas de bloques.

        Retorna:
        - blocks: Lista de bloques con sus respectivas formas.
        """
        blocks = [
            Block(1, "I", [[1, 1, 1, 1]]),
            Block(2, "O", [[1, 1], [1, 1]]),
            Block(3, "T", [[0, 1, 0], [1, 1, 1]]),
            Block(4, "L", [[1, 0, 0], [1, 1, 1]]),
            Block(5, "S", [[0, 1, 1], [1, 1, 0]]),
            Block(6, "Z", [[1, 1, 0], [0, 1, 1]]),
            Block(7, "J", [[0, 0, 1], [1, 1, 1]]),
        ]
        return blocks
