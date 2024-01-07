import pygame
import os


class Background:
    def __init__(self, screen_width, screen_height, image_path):
        """
        Inicializa la clase Background.

        Parámetros:
        - screen_width: Ancho de la pantalla.
        - screen_height: Altura de la pantalla.
        - image_path: Ruta de la imagen de fondo.
        """
        # Cargar y escalar la imagen
        self.image = self.load_and_scale_image(image_path, screen_width, screen_height)

        # Obtener el rectángulo de la imagen y centrarlo en la pantalla
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height // 2))

    def load_and_scale_image(self, image_path, screen_width, screen_height):
        """
        Carga y escala la imagen para que llene la pantalla.

        Parámetros:
        - image_path: Ruta de la imagen de fondo.
        - screen_width: Ancho de la pantalla.
        - screen_height: Altura de la pantalla.

        Devuelve:
        - Imagen escalada.
        """
        # Cargar la imagen original
        original_background_image = pygame.image.load(image_path)

        # Obtener las dimensiones originales de la imagen
        original_width, original_height = original_background_image.get_size()

        # Calcular el factor de escala para ajustar la imagen a la pantalla
        scale_factor_width = screen_width / original_width
        scale_factor_height = screen_height / original_height

        # Elegir el factor de escala más grande para que la imagen llene completamente la pantalla
        scale_factor = max(scale_factor_width, scale_factor_height)

        # Escalar la imagen
        scaled_image = pygame.transform.scale(
            original_background_image,
            (int(original_width * scale_factor), int(original_height * scale_factor)),
        )

        return scaled_image

    def draw(self, screen):
        """
        Dibuja la imagen de fondo en la pantalla.

        Parámetros:
        - screen: Superficie de la pantalla de Pygame.
        """
        # Dibujar la imagen en la posición del rectángulo
        screen.blit(self.image, self.rect)
