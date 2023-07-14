from typing import TYPE_CHECKING
from figures.Figure import Figure
from figures.Rook import Rook
from figures.Bishop import Bishop
from Colour import Colour

if TYPE_CHECKING:
    from Chessboard import Chessboard


class Queen(Figure):
    def __init__(self, colour: Colour):
        super().__init__(colour)

    def get_moves(self, position: tuple[int, int], chessboard: "Chessboard") -> list[tuple[int, int]]:
        rook = Rook(self.colour)
        bishop = Bishop(self.colour)

        return [*rook.get_moves(position, chessboard), *bishop.get_moves(position, chessboard)]
