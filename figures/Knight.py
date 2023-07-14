from typing import TYPE_CHECKING
from figures.Figure import Figure
from Colour import Colour

if TYPE_CHECKING:
    from Chessboard import Chessboard


class Knight(Figure):
    def __init__(self, colour: Colour):
        super().__init__(colour)

    def get_moves(self, position: tuple[int, int], chessboard: "Chessboard") -> list[tuple[int, int]]:
        moves = []
        x, y = position

        if x + 1 < 8:
            if y + 2 < 8:
                figure = chessboard.get_figure_from_position((x + 1, y + 2))
                if figure is None or figure.colour is not self.colour:
                    moves.append((x + 1, y + 2))

            if y - 2 >= 0:
                figure = chessboard.get_figure_from_position((x + 1, y - 2))
                if figure is None or figure.colour is not self.colour:
                    moves.append((x + 1, y - 2))

        if x + 2 < 8:
            if y + 1 < 8:
                figure = chessboard.get_figure_from_position((x + 2, y + 1))
                if figure is None or figure.colour is not self.colour:
                    moves.append((x + 2, y + 1))

            if y - 1 >= 0:
                figure = chessboard.get_figure_from_position((x + 2, y - 1))
                if figure is None or figure.colour is not self.colour:
                    moves.append((x + 2, y - 1))

        if x - 1 >= 0:
            if y + 2 < 8:
                figure = chessboard.get_figure_from_position((x - 1, y + 2))
                if figure is None or figure.colour is not self.colour:
                    moves.append((x - 1, y + 2))

            if y - 2 >= 0:
                figure = chessboard.get_figure_from_position((x + 1, y - 2))
                if figure is None or figure.colour is not self.colour:
                    moves.append((x - 1, y - 2))

        if x - 2 >= 0:
            if y + 1 < 8:
                figure = chessboard.get_figure_from_position((x - 2, y + 1))
                if figure is None or figure.colour is not self.colour:
                    moves.append((x - 2, y + 1))

            if y - 1 >= 0:
                figure = chessboard.get_figure_from_position((x - 2, y - 1))
                if figure is None or figure.colour is not self.colour:
                    moves.append((x - 2, y - 1))

        return moves
