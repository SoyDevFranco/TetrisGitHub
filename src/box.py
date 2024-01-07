# box.py
import pygame
from constantes import Colors


class Box:
    def __init__(self, name, position_x, position_y, width, height, color):
        self.name = name
        self.rect = pygame.Rect(position_x, position_y, width, height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 3)

    def get_center(self):
        """Obtiene las coordenadas del centro del rectángulo."""
        center_x = self.rect.x + self.rect.width // 2
        center_y = self.rect.y + self.rect.height // 2
        return center_x, center_y
