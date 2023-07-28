from typing import Optional
from figures.Figure import Figure
from figures.Pawn import Pawn
from figures.Rook import Rook
from figures.Knight import Knight
from figures.Bishop import Bishop
from figures.Queen import Queen
from figures.King import King
from Colour import Colour


class Chessboard:
    def __init__(self):
        self.board = [
            [Rook(Colour.WHITE), Knight(Colour.WHITE), Bishop(Colour.WHITE), King(Colour.WHITE), Queen(Colour.WHITE), Bishop(Colour.WHITE), Knight(Colour.WHITE), Rook(Colour.WHITE)],
            [Pawn(Colour.WHITE), Pawn(Colour.WHITE), Pawn(Colour.WHITE), Pawn(Colour.WHITE), Pawn(Colour.WHITE), Pawn(Colour.WHITE), Pawn(Colour.WHITE), Pawn(Colour.WHITE)],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn(Colour.BLACK), Pawn(Colour.BLACK), Pawn(Colour.BLACK), Pawn(Colour.BLACK), Pawn(Colour.BLACK), Pawn(Colour.BLACK), Pawn(Colour.BLACK), Pawn(Colour.BLACK)],
            [Rook(Colour.BLACK), Knight(Colour.BLACK), Bishop(Colour.BLACK), King(Colour.BLACK), Queen(Colour.BLACK), Bishop(Colour.BLACK), Knight(Colour.BLACK), Rook(Colour.BLACK)],
        ]
        self.last_move = ()

    def get_figure_from_position(self, position: tuple[int, int]) -> Optional[Figure]:
        x, y = position

        return self.board[x][y]

    def move_figure(self, start_position: tuple[int, int], end_position: tuple[int, int]) -> None:
        start_x, start_y = start_position
        end_x, end_y = end_position

        figure = self.get_figure_from_position(start_position)

        if isinstance(figure, Pawn) and start_y != end_y and self.get_figure_from_position(end_position) is None:
            self.board[start_x][end_y] = None

        self.board[end_x][end_y] = figure
        self.board[start_x][start_y] = None

        if figure is not None:
            figure.moves.append(end_position)

        if isinstance(figure, King) and abs(start_y - end_y) is 2:
            if end_y < 4:
                self.move_figure((start_x, 0), (start_x, 2))
            else:
                self.move_figure((start_x, 7), (start_x, 4))

        self.last_move = end_position

        if isinstance(figure, Pawn) and ((figure.colour is Colour.WHITE and end_x == 7) or (figure.colour is Colour.BLACK and end_x == 0)):
            queen = Queen(figure.colour)
            queen.moves = figure.moves
            self.board[end_x][end_y] = queen
