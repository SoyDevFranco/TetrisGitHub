# main.py
import pygame
from constantes import *
from drawBoard import *


# Inicialización de Pygame
pygame.init()

# Inicializar ventana y reloj
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
Grid = Grid()
colors = Colors()

while running:
    screen.fill(colors.LIGHT_BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    Grid.draw_board(screen)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
