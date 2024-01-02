# src\main.py
import pygame
from constantes import Colors, Constans
from drawBoard import Grid
from game import Game

constans = Constans()
colors = Colors()
grid = Grid(colors, constans)
game = Game(grid, colors)

constans = Constans()
pygame.init()

screen = pygame.display.set_mode((constans.WIDTH, constans.HEIGHT))
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
                if game.check_collision(
                    game.current_block.position_block_x,
                    game.current_block.position_block_y + 1,
                ):
                    game.solidify_block()
                    game.current_block = game.next_block
                    game.next_block = game.get_random_block()

    # Dibujar el tablero y la pieza actual
    grid.draw_board(screen)
    game.current_block.draw_shape(screen)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
