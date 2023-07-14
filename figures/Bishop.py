from typing import Optional, TYPE_CHECKING

from Colour import Colour
from figures.Figure import Figure

if TYPE_CHECKING:
    from Chessboard import Chessboard


class Bishop(Figure):

    def __init__(self, colour: Colour):
        super().__init__(colour)

    def get_moves(self, position: tuple[int, int], chessboard: "Chessboard") -> list[list[tuple[int, int]]]:
        return [*self._get_moves_top_right(position, chessboard), *self._get_moves_bottom_right(position, chessboard),
                *self._get_moves_bottom_left(position, chessboard), *self._get_moves_top_left(position, chessboard)]

    def _get_moves_top_right(self, position: tuple[int, int], chessboard: "Chessboard") -> Optional[
        list[tuple[int, int]]]:
        x, y = position
        if x + 1 < 8 and y + 1 < 8:
            if chessboard.get_figure_from_position((x + 1, y + 1)) is None:
                return [(x + 1, y + 1), *self._get_moves_top_right((x + 1, y + 1), chessboard)]
            elif chessboard.get_figure_from_position((x + 1, y + 1)).colour != self.colour:
                return [(x + 1, y + 1)]
        return []

    def _get_moves_bottom_right(self, position: tuple[int, int], chessboard: "Chessboard") -> Optional[
        list[tuple[int, int]]]:
        x, y = position

        if x + 1 >= 0 and y - 1 >= 0:
            if chessboard.get_figure_from_position((x + 1, y - 1)) is None:
                return [(x + 1, y - 1), *self._get_moves_bottom_right((x + 1, y - 1), chessboard)]
            elif chessboard.get_figure_from_position((x + 1, y - 1)).colour != self.colour:
                return [(x + 1, y - 1)]
        return []

    def _get_moves_bottom_left(self, position: tuple[int, int], chessboard: "Chessboard") -> Optional[
        list[tuple[int, int]]]:
        x, y = position

        if x - 1 >= 0 and y - 1 >= 0:
            if chessboard.get_figure_from_position((x - 1, y - 1)) is None:
                return [(x - 1, y - 1), *self._get_moves_bottom_left((x - 1, y - 1), chessboard)]
            elif chessboard.get_figure_from_position((x - 1, y - 1)).colour != self.colour:
                return [(x - 1, y - 1)]
        return []

    def _get_moves_top_left(self, position: tuple[int, int], chessboard: "Chessboard") -> Optional[
        list[tuple[int, int]]]:
        x, y = position

        if x - 1 >= 0 and y + 1 < 8:
            if chessboard.get_figure_from_position((x - 1, y + 1)) is None:
                return [(x - 1, y + 1), *self._get_moves_top_left((x - 1, y + 1), chessboard)]
            elif chessboard.get_figure_from_position((x - 1, y + 1)).colour != self.colour:
                return [(x - 1, y + 1)]
        return []
