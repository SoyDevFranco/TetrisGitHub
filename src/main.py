# main.py
import pygame
from constantes import *
from drawBoard import *
from block import *
from game import *

# Inicialización de Pygame
pygame.init()

# Inicializar ventana y reloj
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

colors = Colors()
grid = Grid(colors)
game = Game(
    grid,
)

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

    grid.draw_board(screen)
    current_block = game.current_block
    current_block.draw_shape(screen, grid, colors)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
