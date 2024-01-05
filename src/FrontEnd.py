# frontend.py
import pygame


class ScoreManager:
    def __init__(self):
        """
        Inicializa un objeto ScoreManager.

        Atributos:
        - score: Puntuación actual del juego.
        """
        self.score = 0

    def increase_score(self, points):
        """
        Aumenta la puntuación actual.

        Parámetros:
        - points: Puntos a añadir a la puntuación.
        """
        self.score += points

    def reset_score(self):
        """Resetea la puntuación a cero."""
        self.score = 0

    def get_score(self):
        """Obtiene la puntuación actual."""
        return self.score


class NextBlockDisplay:
    def __init__(self, screen, grid, next_block):
        """
        Inicializa un objeto NextBlockDisplay.

        Parámetros:
        - screen: Superficie de la pantalla de pygame.
        - grid: Instancia de la clase Grid.
        - next_block: Bloque siguiente a ser mostrado en la ventana lateral.
        """
        self.screen = screen
        self.grid = grid
        self.next_block = next_block
        self.cell_size = 20

    def draw_next_block(self):
        """
        Dibuja el próximo bloque en la ventana lateral.

        Esta función debe ser implementada con la lógica específica
        para dibujar el bloque en la posición deseada en la ventana lateral.
        """
        pass


class AudioManager:
    def __init__(self):
        """
        Inicializa un objeto AudioManager para gestionar los sonidos del juego.
        """
        pygame.mixer.init()
        self.music = pygame.mixer.Sound("Tetris_theme.mp3")  # Música del juego
        self.music.set_volume(0.5)

        # Sonidos adicionales
        self.clear_row_sound = pygame.mixer.Sound("clear_row_sound.mp3")
        self.clear_rows_sound = pygame.mixer.Sound("clear_rows_sound.mp3")
        self.block_lock_sound = pygame.mixer.Sound("block_lock_sound.mp3")
        self.game_over_sound = pygame.mixer.Sound("game_over_sound.mp3")
        self.next_level = pygame.mixer.Sound("next_level.mp3")
        self.scores = pygame.mixer.Sound("scores.mp3")

    def play_music(self):
        """Reproduce la música del juego en bucle."""
        self.music.play(-1)

    def stop_music(self):
        """Detiene la reproducción de la música del juego."""
        self.music.stop()

    def play_clear_row_sound(self):
        """Reproduce el sonido cuando se elimina una fila."""
        self.clear_row_sound.play()

    def play_clear_rows_sound(self):
        """Reproduce el sonido cuando se eliminan múltiples filas a la vez."""
        self.clear_rows_sound.play()

    def play_block_lock_sound(self):
        """Reproduce el sonido cuando un bloque se solidifica en el tablero."""
        self.block_lock_sound.play()

    def play_game_over_sound(self):
        """Reproduce el sonido cuando el juego termina."""
        self.game_over_sound.play()

    def stop_sound(self):
        """Detiene la reproducción de todos los sonidos."""
        pygame.mixer.stop()
