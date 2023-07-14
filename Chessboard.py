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

    def get_figure_from_position(self, position: tuple[int, int]) -> Optional[Figure]:
        x, y = position
        return self.board[x][y]

    def move_figure(self, start_position: tuple[int, int], end_position: tuple[int, int]):
        start_x, start_y = start_position
        end_x, end_y = end_position
        figure = self.get_figure_from_position(start_position)
        if figure and hasattr(figure, "has_moved"):
            figure.has_moved = True
        self.board[end_x][end_y] = figure
        self.board[start_x][start_y] = None
