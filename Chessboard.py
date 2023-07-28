from typing import Optional

from Colour import Colour
from figures.Bishop import Bishop
from figures.Figure import Figure
from figures.King import King
from figures.Knight import Knight
from figures.Pawn import Pawn
from figures.Queen import Queen
from figures.Rook import Rook


def _place_figures() -> list[list[Optional[Figure]]]:
    return [
        [Rook(Colour.WHITE), Knight(Colour.WHITE), Bishop(Colour.WHITE), King(Colour.WHITE), Queen(Colour.WHITE),
         Bishop(Colour.WHITE), Knight(Colour.WHITE), Rook(Colour.WHITE)],
        [Pawn(Colour.WHITE), Pawn(Colour.WHITE), Pawn(Colour.WHITE), Pawn(Colour.WHITE), Pawn(Colour.WHITE),
         Pawn(Colour.WHITE), Pawn(Colour.WHITE), Pawn(Colour.WHITE)],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [Pawn(Colour.BLACK), Pawn(Colour.BLACK), Pawn(Colour.BLACK), Pawn(Colour.BLACK), Pawn(Colour.BLACK),
         Pawn(Colour.BLACK), Pawn(Colour.BLACK), Pawn(Colour.BLACK)],
        [Rook(Colour.BLACK), Knight(Colour.BLACK), Bishop(Colour.BLACK), King(Colour.BLACK), Queen(Colour.BLACK),
         Bishop(Colour.BLACK), Knight(Colour.BLACK), Rook(Colour.BLACK)],
    ]


class Chessboard:
    def __init__(self):
        self.board = _place_figures()
        self.last_move = ()

    def get_figure_from_position(self, position: tuple[int, int]) -> Optional[Figure]:
        x, y = position
        return self.board[x][y]

    def _promote(self, figure: Pawn, pos_x: int, pos_y: int):
        queen = Queen(figure.colour)
        queen.moves = figure.moves
        self.board[pos_x][pos_y] = queen

    def move_figure(self, start_position: tuple[int, int], end_position: tuple[int, int]):
        start_x, start_y = start_position
        end_x, end_y = end_position
        figure = self.get_figure_from_position(start_position)

        # En passant
        if isinstance(figure, Pawn) and start_y != end_y and self.get_figure_from_position(end_position) is None:
            self.board[start_x][end_y] = None

        self.board[end_x][end_y] = figure
        self.board[start_x][start_y] = None

        # Castling
        if isinstance(figure, King) and abs(start_y - end_y) == 2:
            if end_y < 4:
                self.move_figure((start_x, 0), (start_x, 2))
            else:
                self.move_figure((start_x, 7), (start_x, 4))

        # Save moves to figure
        figure.moves.append(end_position)
        self.last_move = end_position

        # Promotion (defaulted to Queen)
        if isinstance(figure, Pawn) and (figure.colour == Colour.WHITE and end_x == 7) or (
                figure.colour == Colour.BLACK and end_x == 0):
            self._promote(figure, end_x, end_y)
