from typing import Optional, TYPE_CHECKING

from Colour import Colour
from figures.Bishop import Bishop
from figures.Figure import Figure
from figures.Rook import Rook

if TYPE_CHECKING:
    from Chessboard import Chessboard


class Queen(Figure):

    def __init__(self, colour: Colour):
        super().__init__(colour)

    def get_moves(self, position: tuple[int, int], chessboard: "Chessboard") -> list[list[tuple[int, int]]]:
        rook_moves = Rook(self.colour).get_moves(position, chessboard)
        bishop_moves = Bishop(self.colour).get_moves(position, chessboard)
        return [*rook_moves, *bishop_moves]
