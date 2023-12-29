from constantes import Colors

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
