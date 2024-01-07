# box.py
import pygame


class Box:
    def __init__(self, name, position_x, position_y, width, height, color):
        """
        Inicializa una instancia de la clase Box.

        Parameters:
        - name (str): El nombre de la caja.
        - position_x (int): La posición horizontal de la caja.
        - position_y (int): La posición vertical de la caja.
        - width (int): El ancho de la caja.
        - height (int): La altura de la caja.
        - color (tuple): El color de la caja en formato (R, G, B).
        """
        self.name = name
        self.rect = pygame.Rect(position_x, position_y, width, height)
        self.color = color

    def draw(self, screen):
        """
        Dibuja la caja en la pantalla.

        Parameters:
        - screen: La superficie de la pantalla de Pygame.
        """
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 3)

    def get_center(self):
        """
        Obtiene las coordenadas del centro del rectángulo.

        Returns:
        - tuple: Las coordenadas (x, y) del centro de la caja.
        """
        center_x = self.rect.x + self.rect.width // 2
        center_y = self.rect.y + self.rect.height // 2
        return center_x, center_y
