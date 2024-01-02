import pygame
from constantes import Colors, Constans
from drawBoard import Grid
from game import Game
from eventHandler import EventHandler

colors = Colors()
<<<<<<< HEAD
<<<<<<< Updated upstream
grid = Grid()
game = Game(grid)
=======
grid = Grid(colors)
game = Game(grid, colors)
running = True  # Variable global
>>>>>>> Stashed changes
=======
grid = Grid()
game = Game(grid)
>>>>>>> parent of 7187403 (va todo en marcha v3)

event_handler = EventHandler(
    game, running
)  # Pasar la variable running al constructor de EventHandler
constans = Constans()
pygame.init()

screen = pygame.display.set_mode((constans.WIDTH, constans.HEIGHT))
clock = pygame.time.Clock()
game_over = False

while running:
    screen.fill(colors.LIGHT_BLUE)
    event_handler.handle_events()

    # Dibujar el tablero y la pieza actual
    grid.draw_board(screen)
    game.current_block.draw_shape(screen)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
