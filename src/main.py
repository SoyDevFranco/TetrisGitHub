# src\main.py # 6.5.1
import pygame
from constantes import Colors, Constants
from drawBoard import Grid
from game import Game

# Configuraciones y objetos del juego
constants = Constants()
colors = Colors()
grid = Grid()
game = Game(grid)

# Inicializar pygame
pygame.init()

# Configuración de la ventana del juego
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("Tetris Game")  # Añade un título a la ventana

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Flags de ejecución
running = True
game_over = False

# Bucle principal del juego
while running:
    screen.fill(colors.light_blue)  # Llena la pantalla con el color de fondo

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
                game.move_up()  # Agrega la lógica para mover hacia arriba si es necesario

    # Dibujar el tablero y la pieza actual
    grid.draw_board(screen)
    game.current_block.draw_shape(screen)

    # Actualizar la ventana después de cada iteración del bucle
    pygame.display.update()

    # Controlar la velocidad del juego
    clock.tick(30)  # Ajusta el número para cambiar la velocidad del juego
