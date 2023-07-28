import pygame

from Chessboard import Chessboard
from Colour import Colour

pygame.init()

SIZE = 100

screen = pygame.display.set_mode((SIZE * 8, SIZE * 8))

running = True

clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.Font("chess.ttf", 80)

chessboard = Chessboard()

is_moving_piece = False
start_position = (0, 0)
current_moves = []


def draw_board() -> None:
    current_colour = Colour.WHITE
    for x, row in enumerate(chessboard.board):
        for y, _ in enumerate(row):
            pygame.draw.rect(screen, current_colour.value, (y * SIZE, x * SIZE, SIZE, SIZE))
            current_colour = Colour.WHITE if current_colour == Colour.BLACK else Colour.BLACK
        current_colour = Colour.WHITE if current_colour == Colour.BLACK else Colour.BLACK


def draw_figures() -> None:
    for x, row in enumerate(chessboard.board):
        for y, field in enumerate(row):
            if field is not None:
                text_surface = font.render(field.get_picture(), True,
                                           (255, 255, 255) if field.colour == Colour.WHITE else (0, 0, 0))
                screen.blit(text_surface, (y * SIZE, x * SIZE))


def draw_moves() -> None:
    for move in current_moves:
        x, y = move
        pygame.draw.rect(screen, (0, 255, 255), (y * SIZE, x * SIZE, SIZE, SIZE))


def mouse_show_moves() -> None:
    global current_moves, is_moving_piece, start_position
    mouse_position = pygame.mouse.get_pos()
    y, x = map(lambda a: a // SIZE, mouse_position)
    figure = chessboard.get_figure_from_position((x, y))
    if figure and figure.colour is (Colour.WHITE if chessboard.whites_turn else Colour.BLACK):
        moves = chessboard.check_possible_moves_for_piece((x, y))
        print(f"{figure}: {moves}")

        if len(moves) > 0:
            start_position = (x, y)
            is_moving_piece = True
            current_moves = moves


def mouse_select_move() -> None:
    global is_moving_piece, current_moves, running
    mouse_position = pygame.mouse.get_pos()
    y, x = map(lambda a: a // SIZE, mouse_position)
    for curr_x, curr_y in current_moves:
        if curr_x == x and curr_y == y:
            chessboard.move_figure(start_position, (x, y))
            if chessboard.check_check():
                print("Check!")
                if chessboard.check_checkmate():
                    print("Checkmate!")
                    running = False
            elif chessboard.check_stalemate():
                print("Stalemate!")
                running = False

            chessboard.whites_turn = not chessboard.whites_turn
    is_moving_piece = False
    current_moves = []


while running:
    screen.fill((0, 0, 0))
    draw_board()

    for event in pygame.event.get():
        if not is_moving_piece and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_show_moves()
        elif is_moving_piece and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_select_move()

        if event.type == pygame.QUIT:
            running = False

    draw_moves()
    draw_figures()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
