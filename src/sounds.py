# sounds.py
import pygame


class AudioManager:
    def __init__(self):
        """
        Inicializa un objeto AudioManager para gestionar los sonidos del juego.
        """
        pygame.mixer.init()

        # Música del juego
        self.music = pygame.mixer.Sound("sounds/Tetris_theme.mp3")
        self.music.set_volume(0.10)

        # Sonidos adicionales con ajustes de volumen
        self.clear_row_sound = pygame.mixer.Sound("sounds/clear_row_sound.mp3")
        self.clear_row_sound.set_volume(0.6)  # Ajusta el volumen según sea necesario

        self.block_lock_sound = pygame.mixer.Sound("sounds/block_lock_sound.mp3")
        self.block_lock_sound.set_volume(0.1)  # Ajusta el volumen según sea necesario

        self.game_over_sound = pygame.mixer.Sound("sounds/game_over_sound.mp3")
        self.game_over_sound.set_volume(0.2)  # Ajusta el volumen según sea necesario

    def play_music(self):
        """Reproduce la música del juego en bucle."""
        self.music.play(-1)

    def stop_music(self):
        """Detiene la reproducción de la música del juego."""
        self.music.stop()

    def play_clear_row_sound(self):
        """Reproduce el sonido cuando se elimina una fila."""
        self.clear_row_sound.play()

    def play_block_lock_sound(self):
        """Reproduce el sonido cuando un bloque se solidifica en el tablero."""
        self.block_lock_sound.play()

    def play_game_over_sound(self):
        """Reproduce el sonido cuando el juego termina."""
        self.game_over_sound.play()

    def stop_sound(self):
        """Detiene la reproducción de todos los sonidos."""
        pygame.mixer.stop()
