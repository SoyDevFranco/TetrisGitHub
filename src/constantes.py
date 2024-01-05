# Constantes # 6.5.1
class Constants:
    def __init__(self):
        """
        Inicializa una instancia de la clase Constants.

        Atributos:
        - WIDTH: Ancho de la ventana del juego.
        - HEIGHT: Altura de la ventana del juego.
        - BOARD_WIDTH: Número de columnas en el tablero del juego.
        - BOARD_HEIGHT: Número de filas en el tablero del juego.
        - BLOCK_SIZE: Tamaño de un bloque en píxeles.
        """
        self.WIDTH = 900
        self.HEIGHT = 800
        self.BOARD_WIDTH = 10
        self.BOARD_HEIGHT = 20
        self.BLOCK_SIZE = 34


# Colores
class Colors:
    dark_grey = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)

    @classmethod
    def get_cell_colors(cls):
        """
        Devuelve una lista de colores utilizados para representar diferentes celdas en el tablero del juego.

        Retorna:
        - Lista de colores en formato RGB.
        """
        return [
            cls.dark_grey,
            cls.green,
            cls.red,
            cls.orange,
            cls.yellow,
            cls.purple,
            cls.cyan,
            cls.white,
            cls.light_blue,
        ]
