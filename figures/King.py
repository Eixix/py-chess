from typing import TYPE_CHECKING
from figures.Figure import Figure
from Colour import Colour

if TYPE_CHECKING:
    from Chessboard import Chessboard


class King(Figure):
    def __init__(self, colour: Colour):
        super().__init__(colour)
        self.has_moved = False

    def get_moves(self, position: tuple[int, int], chessboard: "Chessboard") -> list[tuple[int, int]]:
        moves = []
        x, y = position

        if x + 1 < 8:
            figure = chessboard.get_figure_from_position((x + 1, y))
            if figure is None or figure.colour is not self.colour:
                moves.append((x + 1, y))

        if x + 1 < 8 and y + 1 < 8:
            figure = chessboard.get_figure_from_position((x + 1, y + 1))
            if figure is None or figure.colour is not self.colour:
                moves.append((x + 1, y + 1))

        if y + 1 < 8:
            figure = chessboard.get_figure_from_position((x, y + 1))
            if figure is None or figure.colour is not self.colour:
                moves.append((x, y + 1))

        if x - 1 >= 0 and y + 1 < 8:
            figure = chessboard.get_figure_from_position((x - 1, y + 1))
            if figure is None or figure.colour is not self.colour:
                moves.append((x - 1, y + 1))

        if x - 1 >= 0:
            figure = chessboard.get_figure_from_position((x - 1, y))
            if figure is None or figure.colour is not self.colour:
                moves.append((x - 1, y))

        if x - 1 >= 0 and y - 1 >= 0:
            figure = chessboard.get_figure_from_position((x - 1, y - 1))
            if figure is None or figure.colour is not self.colour:
                moves.append((x - 1, y - 1))

        if y - 1 >= 0:
            figure = chessboard.get_figure_from_position((x, y - 1))
            if figure is None or figure.colour is not self.colour:
                moves.append((x, y - 1))

        if x + 1 < 8 and y - 1 >= 0:
            figure = chessboard.get_figure_from_position((x + 1, y - 1))
            if figure is None or figure.colour is not self.colour:
                moves.append((x + 1, y - 1))

        return moves
