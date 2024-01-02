import pygame


class EventHandler:
    def __init__(self, game, running):
        self.game = game
        self.running = running  # Referencia a la variable running del módulo principal

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = (
                    False  # Ahora cambia la variable global del módulo principal
                )
            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event)

    def handle_keydown(self, event):
        if event.key == pygame.K_ESCAPE:
            self.game.running = False
        elif event.key == pygame.K_LEFT:
            self.game.move_left()
        elif event.key == pygame.K_RIGHT:
            self.game.move_right()
        elif event.key == pygame.K_DOWN:
            self.game.move_down()
            if self.game.check_collision(
                self.game.current_block.position_block_x,
                self.game.current_block.position_block_y + 1,
            ):
                self.game.solidify_block()
                self.game.current_block = self.game.next_block
                self.game.next_block = self.game.get_random_block()
