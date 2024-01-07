# text.py
import pygame


class TextHandler:
    @staticmethod
    def create_text(surface, content, font_size, color, box, margin):
        """
        Crea un objeto de texto en una superficie dada.

        :param surface: Superficie en la que se creará el texto.
        :param content: Contenido del texto.
        :param font_size: Tamaño de la fuente.
        :param color: Color del texto.
        :param box: Instancia de la clase Box que define la posición del texto.
        :param margin: Margen para ajustar la posición vertical del texto.
        :return: Tupla con la superficie de texto y el rectángulo asociado.
        """
        box_center_x, box_center_y = box.get_center()
        box_center_y += margin  # Ajuste de posición vertical con margen
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(content, True, color)
        text_rect = text_surface.get_rect(center=(box_center_x, box_center_y))
        surface.blit(text_surface, text_rect)
        return surface.blit(text_surface, text_rect)
