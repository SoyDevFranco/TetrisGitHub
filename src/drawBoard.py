# src\drawBoard.py # 6.5.1
import pygame
from constantes import Colors, Constants


class Grid:
    def __init__(self):
        """
        Inicializa una instancia de la clase Grid.

        Atributos:
        - num_cols: Número de columnas en el tablero.
        - num_rows: Número de filas en el tablero.
        - cell_size: Tamaño de cada celda en píxeles.
        - constants: Instancia de la clase Constants para acceder a las constantes del juego.
        - colors: Colores utilizados para representar diferentes celdas en el tablero.
        - grid_position_x: Posición X del tablero en la pantalla.
        - grid_position_y: Posición Y del tablero en la pantalla.
        - grid: Matriz que representa el estado actual del tablero.
        """
        self.num_cols = 10
        self.num_rows = 20
        self.cell_size = 30
        self.constants = Constants()
        self.colors = Colors.get_cell_colors()
        self.grid_position_x = self.calculate_grid_position_x()
        self.grid_position_y = self.calculate_grid_position_y()
        self.grid = [[0] * self.num_cols for _ in range(self.num_rows)]

    def calculate_grid_position_x(self):
        """
        Calcula y devuelve la posición X del tablero en la pantalla.

        Retorna:
        - Posición X del tablero.
        """
        return (self.constants.WIDTH - (self.cell_size * self.num_cols)) // 3.5

    def calculate_grid_position_y(self):
        """
        Calcula y devuelve la posición Y del tablero en la pantalla.

        Retorna:
        - Posición Y del tablero.
        """
        return (self.constants.HEIGHT - (self.cell_size * self.num_rows)) // 2

    def is_inside(self, row, column):
        """
        Verifica si la posición (fila, columna) está dentro de los límites del tablero.

        Parámetros:
        - row: Índice de fila.
        - column: Índice de columna.

        Retorna:
        - True si la posición está dentro de los límites, False de lo contrario.
        """
        return 0 <= row < self.num_rows and 0 <= column < self.num_cols

    def is_empty(self, row, column):
        """
        Verifica si la celda en la posición (fila, columna) está vacía.

        Parámetros:
        - row: Índice de fila.
        - column: Índice de columna.

        Retorna:
        - True si la celda está vacía, False de lo contrario.
        """
        return self.grid[row][column] == 0

    def draw_board(self, screen):
        """
        Dibuja el tablero en la pantalla utilizando pygame.

        Parámetros:
        - screen: Superficie de la pantalla de pygame.
        """
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(
                    col * self.cell_size + self.grid_position_x,
                    row * self.cell_size + self.grid_position_y,
                    self.cell_size,
                    self.cell_size,
                )
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
                pygame.draw.rect(screen, Colors.light_blue, cell_rect, 1)
