# text.py
import pygame


class TextHandler:
    @staticmethod
    def create_text_in_box(surface, content, font_size, color, box, margin):
        """
        Crea un objeto de texto en una superficie dada, dentro de una caja.

        :param surface: Superficie en la que se creará el texto.
        :param content: Contenido del texto.
        :param font_size: Tamaño de la fuente.
        :param color: Color del texto.
        :param box: Instancia de la clase Box que define la posición del texto.
        :param margin: Margen para ajustar la posición vertical del texto.
        :return: Rectángulo asociado al texto en la superficie.
        """
        box_center_x, box_center_y = box.get_center()
        box_center_y += margin  # Ajuste de posición vertical con margen
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(content, True, color)
        text_rect = text_surface.get_rect(center=(box_center_x, box_center_y))
        surface.blit(text_surface, text_rect)
        return text_rect

    @staticmethod
    def create_text_centered(surface, content, font_size, color):
        """
        Crea un objeto de texto en una superficie dada, centrado en la pantalla.

        :param surface: Superficie en la que se creará el texto.
        :param content: Contenido del texto.
        :param font_size: Tamaño de la fuente.
        :param color: Color del texto.
        :return: Rectángulo asociado al texto en el centro de la superficie.
        """
        screen_center_x, screen_center_y = 370, 32.5
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(content, True, color)
        text_rect = text_surface.get_rect(center=(screen_center_x, screen_center_y))
        surface.blit(text_surface, text_rect)
        return text_rect
