import pygame
from Chessboard import Chessboard
from Colour import Colour

pygame.init()

SIZE = 100

screen = pygame.display.set_mode((SIZE * 8, SIZE * 8))

clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.Font('./chess.ttf', 80)

running = True
chessboard = Chessboard()
is_moving_piece = False
current_moves = []
start_position = (0, 0)


def draw_board() -> None:
    field_colour = Colour.WHITE

    for x, row in enumerate(chessboard.board):
        for y, _ in enumerate(row):
            pygame.draw.rect(screen, field_colour.value,
                             (y * SIZE, x * SIZE, SIZE, SIZE))

            field_colour = Colour.WHITE if field_colour is Colour.BLACK else Colour.BLACK

        field_colour = Colour.WHITE if field_colour is Colour.BLACK else Colour.BLACK


def draw_figures() -> None:
    for x, row in enumerate(chessboard.board):
        for y, field in enumerate(row):
            if field is not None:
                text = font.render(field.get_picture(
                ), True, (255, 255, 255) if field.colour is Colour.WHITE else (0, 0, 0))
                screen.blit(text, (y * SIZE, x * SIZE))


def draw_moves() -> None:
    for move in current_moves:
        x, y = move
        pygame.draw.rect(screen, (0, 255, 255),
                         (y * SIZE, x * SIZE, SIZE, SIZE))


def set_current_moves() -> None:
    global current_moves, is_moving_piece, start_position
    mouse_position = pygame.mouse.get_pos()

    y, x = map(lambda x: x // SIZE, mouse_position)

    figure = chessboard.get_figure_from_position((x, y))

    print(figure)

    if figure is not None and figure.colour is (Colour.WHITE if chessboard.whites_turn else Colour.BLACK):
        moves = chessboard.check_possible_moves((x, y))

        print(moves)

        if len(moves) > 0:
            is_moving_piece = True
            current_moves = moves
            start_position = (x, y)


def select_move() -> None:
    global current_moves, is_moving_piece, start_position, running
    mouse_position = pygame.mouse.get_pos()

    y, x = map(lambda x: x // SIZE, mouse_position)

    for move in current_moves:
        if move == (x, y):
            chessboard.move_figure(start_position, (x, y))
            if chessboard.check_check():
                print('check')
                if chessboard.check_checkmate():
                    print('checkmate')
                    running = False
            elif chessboard.check_checkmate():
                print('stalemate')
                running = False

            chessboard.whites_turn = not chessboard.whites_turn

    is_moving_piece = False
    current_moves = []
    start_position = (0, 0)


while running:
    screen.fill((0, 0, 0))
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not is_moving_piece:
                set_current_moves()
            else:
                select_move()

        elif event.type == pygame.QUIT:
            running = False

    draw_moves()
    draw_figures()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
