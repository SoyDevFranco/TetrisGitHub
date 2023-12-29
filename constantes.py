# Constantes
WIDTH, HEIGHT = 900, 800
BOARD_WIDTH, BOARD_HEIGHT = 10, 20
BLOCK_SIZE = 34

# Colores
Colors = {
    "green": (47, 230, 23),
    "red": (232, 18, 18),
    "orange": (226, 116, 17),
    "yellow": (237, 234, 4),
    "purple": (166, 0, 247),
    "cyan": (21, 204, 209),
    "dark_grey": (26, 31, 40),
    "blue": (13, 64, 216),
    "white": (255, 255, 255),
    "dark_blue": (44, 44, 127),
    "light_blue": (59, 85, 162),
    "lavender": (230, 230, 250),
}


class Colors:
    def __init__(self):
        self.GREEN = (47, 230, 23)
        self.RED = (232, 18, 18)
        self.ORANGE = (226, 116, 17)
        self.YELLOW = (237, 234, 4)
        self.PURPLE = (166, 0, 247)
        self.CYAN = (21, 204, 209)
        self.DARK_GREY = (26, 31, 40)
        self.BLUE = (13, 64, 216)
        self.WHITE = (255, 255, 255)
        self.DARK_BLUE = (44, 44, 127)
        self.LIGHT_BLUE = (59, 85, 162)
        self.LAVENDER = (230, 230, 250)


# Definición de piezas de Tetris
pieces = [
    {"name": "Square", "color_piece": Colors["red"], "shape": [[1, 1], [1, 1]]},
    {"name": "Long Bar", "color_piece": Colors["cyan"], "shape": [[1, 1, 1, 1]]},
    {"name": "T", "color_piece": Colors["purple"], "shape": [[0, 1, 0], [1, 1, 1]]},
    {"name": "L", "color_piece": Colors["orange"], "shape": [[1, 0, 0], [1, 1, 1]]},
    {
        "name": "Inverted L",
        "color_piece": Colors["lavender"],
        "shape": [[0, 0, 1], [1, 1, 1]],
    },
    {"name": "S", "color_piece": Colors["green"], "shape": [[0, 1, 1], [1, 1, 0]]},
    {
        "name": "Inverted S",
        "color_piece": Colors["yellow"],
        "shape": [[1, 1, 0], [0, 1, 1]],
    },
]
