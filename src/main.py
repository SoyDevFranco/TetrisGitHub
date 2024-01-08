# Importaciones de módulos y clases
import pygame
from constantes import Colors, Constants
from drawBoard import Grid
from game import Game
from box_factory import BoxFactory
from background import Background
from text import TextHandler
import os
from sounds import AudioManager

# Configuraciones y objetos del juego
constants = Constants()
colors = Colors()
grid = Grid()
audio_manager = AudioManager()
game = Game(grid)

# Puntos iniciales
puntos = 0
text_handler = TextHandler()

# Configuración de la ventana del juego
pygame.init()
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("Tetris Game")

background = Background(
    constants.WIDTH, constants.HEIGHT, os.path.join("img", "background.png")
)

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()
audio_manager.play_music()
# Flags de ejecución
running = True

paused = False
falling_timer = 0

# Bucle principal del juego
while running:
    # Dibujar la imagen de fondo
    background.draw(screen)

    for event in pygame.event.get():
        # Manejar eventos del teclado y ventana
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not paused:  # Solo procesar eventos si el juego no está pausado
                if event.key == pygame.K_LEFT:
                    game.move_left()
                elif event.key == pygame.K_RIGHT:
                    game.move_right()
                elif event.key == pygame.K_DOWN:
                    game.move_down()
                elif event.key == pygame.K_SPACE:
                    game.move_down_hard()
                elif event.key == pygame.K_UP:
                    game.move_up()
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_p:
                paused = not paused
                if paused:
                    audio_manager.stop_music()
                else:
                    audio_manager.play_music()
            if event.key == pygame.K_r:
                game.reset()

    # Dibujar la caja específica por nombre
    puntos += game.calculate_score()

    box_score = BoxFactory.get_box_by_name("box_score")
    if box_score:
        box_score.draw(screen)
        # Mostrar el puntaje en la pantalla
        text_surface = TextHandler.create_text_in_box(
            screen,
            "Puntos: {}".format(puntos),
            30,
            colors.white,
            box_score,
            margin=0,
        )

    box_next_block = BoxFactory.get_box_by_name("box_next_block")
    if box_next_block:
        box_next_block.draw(screen)
        # Mostrar el próximo bloque en la pantalla
        text_surface = TextHandler.create_text_in_box(
            screen, "Próximo Bloque", 30, colors.white, box_next_block, margin=-50
        )

    if paused:
        pause_text_rect = TextHandler.create_text_centered(
            screen, "PAUSA", 60, colors.white
        )

    # Dibujar el tablero y la pieza actual solo si el juego no está pausado

    grid.draw_board(screen)
    # Bucle principal del juego
    falling_timer = game.drop_piece(falling_timer)

    game.current_block.draw_shape(screen)
    game.next_block.draw_shape_preview(screen, box_next_block)

    # Verificar si se ha perdido el juego
    if game.check_loss_condition():
        # Mostrar mensaje de pérdida
        loss_text_rect = TextHandler.create_text_centered(
            screen, "¡Has perdido! Presiona 'r' para reiniciar", 40, colors.white
        )

        # Actualizar la ventana después de mostrar el mensaje de pérdida
        pygame.display.update()

        # Esperar a que el jugador presione 'r' para reiniciar
        game.wait_for_restart(game)
        # Reiniciar el juego
        game.reset()
        puntos = 0
        # Actualizar la ventana después de cada iteración del bucle
    pygame.display.update()

    # Controlar la velocidad del juego
    clock.tick(30)

pygame.quit()
