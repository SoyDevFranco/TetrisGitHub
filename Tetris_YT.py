import pygame
import random

# Constantes
WIDTH, HEIGHT = 900, 800
BOARD_WIDTH, BOARD_HEIGHT = 10, 20
BLOCK_SIZE = 34

# Colores
Colors = {
    "green": (47, 230, 23),
    "red": (232, 18, 18),
    "orange": (226, 116, 17),
    "yellow": (237, 234, 4),
    "purple": (166, 0, 247),
    "cyan": (21, 204, 209),
    "dark_grey": (26, 31, 40),
    "blue": (13, 64, 216),
    "white": (255, 255, 255),
    "dark_blue": (44, 44, 127),
    "light_blue": (59, 85, 162),
    "lavender": (230, 230, 250),
}

# Definición de piezas de Tetris
pieces = [
    {"name": "Square", "color_piece": Colors["red"], "shape": [[1, 1], [1, 1]]},
    {"name": "Long Bar", "color_piece": Colors["cyan"], "shape": [[1, 1, 1, 1]]},
    {"name": "T", "color_piece": Colors["purple"], "shape": [[0, 1, 0], [1, 1, 1]]},
    {"name": "L", "color_piece": Colors["orange"], "shape": [[1, 0, 0], [1, 1, 1]]},
    {
        "name": "Inverted L",
        "color_piece": Colors["lavender"],
        "shape": [[0, 0, 1], [1, 1, 1]],
    },
    {"name": "S", "color_piece": Colors["green"], "shape": [[0, 1, 1], [1, 1, 0]]},
    {
        "name": "Inverted S",
        "color_piece": Colors["yellow"],
        "shape": [[1, 1, 0], [0, 1, 1]],
    },
]

# Inicialización de Pygame
pygame.init()

# Inicializar ventana y reloj
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# Variable de puntaje y tiempo
score = 0
game_over = False
score_font = pygame.font.Font(None, 46)


# Dibujar el puntaje en pantalla
def draw_score(score):
    score_text = score_font.render(f"Puntaje: {score}", True, Colors["white"])
    screen.blit(score_text, (650, 20))


pygame.font.init()

# Lógica del tablero
board = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]

# Calcular posición del tablero en pantalla
center_x = (WIDTH - (BLOCK_SIZE * BOARD_WIDTH)) // 3.5
center_y = (HEIGHT - (BLOCK_SIZE * BOARD_HEIGHT)) // 2


def draw_board(board):
    """Dibuja el tablero en la pantalla."""
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            x, y = (center_x + col * BLOCK_SIZE), (center_y + row * BLOCK_SIZE)
            cell_value = board[row][col]
            color = Colors["dark_grey"] if cell_value == 0 else cell_value

            pygame.draw.rect(screen, color, (x, y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(
                screen, Colors["light_blue"], (x, y, BLOCK_SIZE, BLOCK_SIZE), 1
            )


def draw_shape(piece, position):
    """Dibuja la forma de una pieza en la pantalla."""
    for row in range(len(piece["shape"])):
        for col in range(len(piece["shape"][0])):
            if piece["shape"][row][col] == 1:
                board_row = position[1] + row
                board_col = position[0] + col
                pygame.draw.rect(
                    screen,
                    piece["color_piece"],
                    (
                        center_x + board_col * BLOCK_SIZE,
                        center_y + board_row * BLOCK_SIZE,
                        BLOCK_SIZE,
                        BLOCK_SIZE,
                    ),
                )
                pygame.draw.rect(
                    screen,
                    Colors["light_blue"],
                    (
                        center_x + board_col * BLOCK_SIZE,
                        center_y + board_row * BLOCK_SIZE,
                        BLOCK_SIZE,
                        BLOCK_SIZE,
                    ),
                    1,
                )


def move_piece(current_block, dx, dy):
    """Mueve la pieza actual en la dirección especificada."""
    next_move_x = current_block["position_x"] + dx
    next_move_y = current_block["position_y"] + dy
    if not check_collision(board, current_block, (next_move_x, next_move_y)):
        current_block["position_x"] = next_move_x
        current_block["position_y"] = next_move_y


def check_collision(board, current_block, position):
    """Verifica si hay colisión entre la pieza actual y el tablero."""
    for row_index, row in enumerate(current_block["shape"]):
        for col_index, cell in enumerate(row):
            if cell != 0:
                block_col = position[0] + col_index
                block_row = position[1] + row_index

                # Verificar si el bloque está dentro del rango del tablero
                if len(board) <= block_row < 2 * len(board) and 0 <= block_col < len(
                    board[0]
                ):  # Verificar colisión con bloques existentes en el tablero
                    if board[block_row][block_col] != 0:
                        return True
                else:
                    # Si está fuera del rango del tablero, hay colisión
                    return True
    return False


def solidify_block(board, current_block, position):
    """Solidifica la pieza actual en el tablero."""
    for row_index, row in enumerate(current_block["shape"]):
        for col_index, cell in enumerate(row):
            if cell != 0:
                block_col = position[0] + col_index
                block_row = position[1] + row_index
                board[block_row][block_col] = current_block["color_piece"]

                # Verificar si la pieza se solidificó en las primeras dos filas
                if block_row < 2:
                    global game_over
                    game_over = True


falling_timer = 0


def drop_piece(current_block):
    """Hace caer la pieza actual hacia abajo."""
    global falling_timer
    if pygame.time.get_ticks() - falling_timer >= 1000:
        next_position_y = current_block["position_y"] + 1

        if not check_collision(
            board,
            current_block,
            (current_block["position_x"], next_position_y),
        ):
            current_block["position_y"] = next_position_y
        else:
            solidify_block(
                board,
                current_block,
                (current_block["position_x"], current_block["position_y"]),
            )
            spawn_next_block()

        falling_timer = pygame.time.get_ticks()


# Lista para almacenar las piezas usadas
used_pieces = []


def random_block(pieces, used_pieces):
    """Genera una pieza aleatoria que no ha sido utilizada recientemente."""
    available_pieces = [piece for piece in pieces if piece["name"] not in used_pieces]

    if not available_pieces:
        used_pieces.clear()
        available_pieces = pieces

    random_piece = random.choice(available_pieces)
    used_pieces.append(random_piece["name"])

    return {
        "name": random_piece["name"],
        "color_piece": random_piece["color_piece"],
        "position_x": 4,
        "position_y": 0,
        "shape": random_piece["shape"],
    }


current_block = random_block(pieces, used_pieces)
next_block = random_block(pieces, used_pieces)


def spawn_next_block():
    """Genera y asigna la siguiente pieza."""
    global current_block, next_block
    current_block = next_block
    next_block = random_block(pieces, used_pieces)


def clear_complete_rows(board):
    """Limpia las filas completas del tablero."""
    rows_to_clear = [row for row in range(BOARD_HEIGHT) if all(board[row])]

    for row in rows_to_clear:
        # Establecer la fila completa en 0
        board[row] = [0] * BOARD_WIDTH

    # Mover todas las filas por encima hacia abajo
    for row in reversed(rows_to_clear):
        board.pop(row)
        board.insert(0, [0] * BOARD_WIDTH)

    return len(rows_to_clear)


def rotate_piece(current_block):
    """
    Rota la forma de un bloque en sentido antihorario intercambiando filas y columnas.

    Parameters:
    - current_block: Diccionario que representa el bloque actual.

    Modifica el diccionario current_block actualizando su forma y posición.
    """
    # Construir la forma rotada intercambiando filas y columnas
    rotated_shape = []

    for col in range(len(current_block["shape"][0])):
        rotated_column = []
        for row in range(len(current_block["shape"]) - 1, -1, -1):
            rotated_column.append(current_block["shape"][row][col])
        rotated_shape.append(rotated_column)

    # Calcular el nuevo índice de la columna máxima
    max_col_index = current_block["position_x"] + len(rotated_shape[0])

    # Ajustar la posición del bloque para mantenerlo dentro del rango del tablero
    if max_col_index <= BOARD_WIDTH and max_col_index >= 0:
        current_block["shape"] = rotated_shape
        current_block["position_x"] = min(
            current_block["position_x"], BOARD_WIDTH - len(rotated_shape[0])
        )


while running:
    screen.fill(Colors["light_blue"])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                move_piece(current_block, -1, 0)
            elif event.key == pygame.K_RIGHT:
                move_piece(current_block, 1, 0)
            elif event.key == pygame.K_DOWN:
                move_piece(current_block, 0, 1)
                # Verificar si hay colisión después de mover hacia abajo
                if check_collision(
                    board,
                    current_block,
                    (current_block["position_x"], current_block["position_y"] + 1),
                ):
                    # Si hay colisión, solidificar la pieza y limpiar filas completas
                    solidify_block(
                        board,
                        current_block,
                        (current_block["position_x"], current_block["position_y"]),
                    )
                    clear_complete_rows(board)
                    spawn_next_block()
            elif event.key == pygame.K_SPACE:
                while not check_collision(
                    board,
                    current_block,
                    (current_block["position_x"], current_block["position_y"] + 1),
                ):
                    current_block["position_y"] += 1
                solidify_block(
                    board,
                    current_block,
                    (current_block["position_x"], current_block["position_y"]),
                )
                spawn_next_block()
                clear_complete_rows(board)
            if event.key == pygame.K_UP:
                rotate_piece(current_block)

    draw_board(board)
    draw_shape(
        current_block, (current_block["position_x"], current_block["position_y"])
    )
    drop_piece(current_block)
    draw_score(score)

    # Verificar si el juego ha terminado
    if game_over:
        game_over_text = pygame.font.Font(None, 72).render(
            "Game Over", True, Colors["white"]
        )
        screen.blit(game_over_text, (WIDTH // 3, HEIGHT // 2))
        pygame.display.update()
        pygame.time.wait(2000)  # Esperar 2000 milisegundos (2 segundos)
        running = False

    pygame.display.update()
    clock.tick(30)

pygame.quit()
