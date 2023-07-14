from typing import Optional, TYPE_CHECKING

from Colour import Colour
from figures.Figure import Figure

if TYPE_CHECKING:
    from Chessboard import Chessboard


class Rook(Figure):

    def __init__(self, colour: Colour):
        super().__init__(colour)
        self.has_moved = False

    def get_picture(self):
        return "♖" if self.colour == Colour.WHITE else "♜"

    def get_moves(self, position: tuple[int, int], chessboard: "Chessboard") -> list[list[tuple[int, int]]]:
        return [*self._get_moves_top(position, chessboard), *self._get_moves_bottom(position, chessboard),
                *self._get_moves_left(position, chessboard), *self._get_moves_right(position, chessboard)]

    def _get_moves_top(self, position: tuple[int, int], chessboard: "Chessboard") -> Optional[list[tuple[int, int]]]:
        x, y = position
        if x + 1 < 8:
            if chessboard.get_figure_from_position((x + 1, y)) is None:
                return [(x + 1, y), *self._get_moves_top((x + 1, y), chessboard)]
            elif chessboard.get_figure_from_position((x + 1, y)).colour != self.colour:
                return [(x + 1, y)]
        return []

    def _get_moves_bottom(self, position: tuple[int, int], chessboard: "Chessboard") -> Optional[list[tuple[int, int]]]:
        x, y = position

        if x - 1 >= 0:
            if chessboard.get_figure_from_position((x - 1, y)) is None:
                return [(x - 1, y), *self._get_moves_bottom((x - 1, y), chessboard)]
            elif chessboard.get_figure_from_position((x - 1, y)).colour != self.colour:
                return [(x - 1, y)]
        return []

    def _get_moves_left(self, position: tuple[int, int], chessboard: "Chessboard") -> Optional[list[tuple[int, int]]]:
        x, y = position

        if y - 1 >= 0:
            if chessboard.get_figure_from_position((x, y - 1)) is None:
                return [(x, y - 1), *self._get_moves_left((x, y - 1), chessboard)]
            elif chessboard.get_figure_from_position((x, y - 1)).colour != self.colour:
                return [(x, y - 1)]
        return []

    def _get_moves_right(self, position: tuple[int, int], chessboard: "Chessboard") -> Optional[list[tuple[int, int]]]:
        x, y = position

        if y + 1 < 8:
            if chessboard.get_figure_from_position((x, y + 1)) is None:
                return [(x, y + 1), *self._get_moves_right((x, y + 1), chessboard)]
            elif chessboard.get_figure_from_position((x, y + 1)).colour != self.colour:
                return [(x, y + 1)]
        return []
