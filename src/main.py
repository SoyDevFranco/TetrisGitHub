import pygame
from constantes import Colors, Constants
from drawBoard import Grid
from game import Game
from box_factory import BoxFactory
from background import Background
from text import TextHandler
import os

# Configuraciones y objetos del juego
constants = Constants()
colors = Colors()
grid = Grid()
game = Game(grid)

# Puntos iniciales
puntos = 0
textHandler = TextHandler()

# Configuración de la ventana del juego
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("Tetris Game")

# Inicializar pygame
pygame.init()
background = Background(
    constants.WIDTH, constants.HEIGHT, os.path.join("img", "background.png")
)

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Flags de ejecución
running = True

# Bucle principal del juego
while running:
    # Dibujar la imagen de fondo
    background.draw(screen)

    for event in pygame.event.get():
        # Manejar eventos del teclado y ventana
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()
            if event.key == pygame.K_SPACE:
                game.move_down_hard()
            if event.key == pygame.K_UP:
                game.move_up()

    # Dibujar la caja específica por nombre
    box_score = BoxFactory.get_box_by_name("box_score")
    if box_score:
        box_score.draw(screen)
        text_surface = TextHandler.create_text(
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
        text_surface = TextHandler.create_text(
            screen, "Próximo Bloque", 30, colors.white, box_next_block, margin=-50
        )

    # Dibujar el tablero y la pieza actual
    grid.draw_board(screen)
    game.current_block.draw_shape(screen)
    game.next_block.draw_shape_preview(screen, box_next_block)
    grid.clear_full_rows()

    # Actualizar la ventana después de cada iteración del bucle
    pygame.display.update()

    # Controlar la velocidad del juego
    clock.tick(30)

pygame.quit()
