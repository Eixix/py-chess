from typing import Optional, TYPE_CHECKING

from Colour import Colour
from figures.Figure import Figure

if TYPE_CHECKING:
    from Chessboard import Chessboard


class King(Figure):

    def __init__(self, colour: Colour):
        super().__init__(colour)
        self.has_moved = False

    def get_moves(self, position: tuple[int, int], chessboard: "Chessboard") -> list[list[tuple[int, int]]]:
        moves = []
        x, y = position

        if x + 1 < 8 and (
                chessboard.get_figure_from_position((x + 1, y)) is None or chessboard.get_figure_from_position(
            (x + 1, y)).colour != self.colour):
            moves.append((x + 1, y))
        if x + 1 < 8 and y + 1 < 8 and (
                chessboard.get_figure_from_position((x + 1, y + 1)) is None or chessboard.get_figure_from_position(
            (x + 1, y + 1)).colour != self.colour):
            moves.append((x + 1, y + 1))
        if x + 1 < 8 and y - 1 >= 0 and (
                chessboard.get_figure_from_position((x + 1, y - 1)) is None or chessboard.get_figure_from_position(
            (x + 1, y - 1)).colour != self.colour):
            moves.append((x + 1, y - 1))
        if y + 1 < 8 and (
                chessboard.get_figure_from_position((x, y + 1)) is None or chessboard.get_figure_from_position(
            (x, y + 1)).colour != self.colour):
            moves.append((x, y + 1))
        if y - 1 < 8 and (
                chessboard.get_figure_from_position((x, y - 1)) is None or chessboard.get_figure_from_position(
            (x, y - 1)).colour != self.colour):
            moves.append((x, y - 1))
        if x - 1 >= 0 and (
                chessboard.get_figure_from_position((x - 1, y)) is None or chessboard.get_figure_from_position(
            (x - 1, y)).colour != self.colour):
            moves.append((x - 1, y))
        if x - 1 >= 0 and y + 1 < 8 and (
                chessboard.get_figure_from_position((x - 1, y + 1)) is None or chessboard.get_figure_from_position(
            (x - 1, y + 1)).colour != self.colour):
            moves.append((x - 1, y + 1))
        if x - 1 >= 0 and y - 1 >= 0 and (
                chessboard.get_figure_from_position((x - 1, y - 1)) is None or chessboard.get_figure_from_position(
            (x - 1, y - 1)).colour != self.colour):
            moves.append((x - 1, y - 1))

        return moves
