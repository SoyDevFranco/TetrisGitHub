# src\main.py
import pygame
from constantes import Colors, Constants
from drawBoard import Grid
from game import Game

constants = Constants()
colors = Colors()
grid = Grid()
game = Game(grid)


pygame.init()
# Crear la ventana del juego
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
clock = pygame.time.Clock()
running = True
game_over = False

while running:
    screen.fill(colors.LIGHT_BLUE)

    for event in pygame.event.get():
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
            if event.key == pygame.K_UP:
                game.move_up()

    # Dibujar el tablero y la pieza actual
    grid.draw_board(screen)
    game.current_block.draw_shape(screen)

    # Actualizar el tablero después de solidificar la pieza
    pygame.display.update()

    # Ajustar la velocidad del juego
    clock.tick(30)
