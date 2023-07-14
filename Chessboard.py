from typing import Optional

from Colour import Colour
from figures.Bishop import Bishop
from figures.Figure import Figure
from figures.King import King
from figures.Knight import Knight
from figures.Pawn import Pawn


class Chessboard:
    def __init__(self):
        self.board = self._place_figures()

    def get_figure_from_position(self, position: tuple[int, int]) -> Optional[Figure]:
        x, y = position
        return self.board[x][y]

    def _place_figures(self) -> list[list[Optional[Figure]]]:
        return [
            [None, None, None, None, None, None, None, None],
            [None, Pawn(Colour.WHITE), None, None, None, None, None, None],
            [None, None, Pawn(Colour.WHITE), None, None, None, None, None],
            [None, None, None, Bishop(Colour.BLACK), None, None, None, None],
            [None, None, None, King(Colour.BLACK), Pawn(Colour.BLACK), None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ]
