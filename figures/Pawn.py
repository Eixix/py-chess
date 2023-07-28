from typing import TYPE_CHECKING
from figures.Figure import Figure
from Colour import Colour

if TYPE_CHECKING:
    from Chessboard import Chessboard


class Pawn(Figure):
    def __init__(self, colour: Colour):
        super().__init__(colour)

    def get_picture(self):
        return '♙' if self.colour is Colour.WHITE else '♟︎'

    def get_moves(self, position: tuple[int, int], chessboard: "Chessboard") -> list[tuple[int, int]]:
        moves = []
        x, y = position

        if self.colour == Colour.WHITE:
            if x + 1 < 8 and chessboard.get_figure_from_position((x + 1, y)) is None:
                moves.append((x + 1, y))

                if not self.moves and chessboard.get_figure_from_position((x + 2, y)) is None:
                    moves.append((x + 2, y))

            if x + 1 < 8:
                if y + 1 < 8:
                    figure = chessboard.get_figure_from_position(
                        (x + 1, y + 1))
                    if figure is not None and figure.colour is not self.colour:
                        moves.append((x + 1, y + 1))

                if y - 1 < 8:
                    figure = chessboard.get_figure_from_position(
                        (x + 1, y - 1))
                    if figure is not None and figure.colour is not self.colour:
                        moves.append((x + 1, y - 1))

            if x is 4:
                figure = chessboard.get_figure_from_position((x, y + 1))
                if isinstance(figure, Pawn) and len(figure.moves) == 1 and (x, y + 1) == chessboard.last_move:
                    moves.append((x + 1, y + 1))

                figure = chessboard.get_figure_from_position((x, y - 1))
                if isinstance(figure, Pawn) and len(figure.moves) == 1 and (x, y - 1) == chessboard.last_move:
                    moves.append((x + 1, y - 1))
        else:
            if x - 1 >= 0 and chessboard.get_figure_from_position((x - 1, y)) is None:
                moves.append((x - 1, y))

                if not self.moves and chessboard.get_figure_from_position((x - 2, y)) is None:
                    moves.append((x - 2, y))

            if x - 1 >= 0:
                if y + 1 < 8:
                    figure = chessboard.get_figure_from_position(
                        (x - 1, y + 1))
                    if figure is not None and figure.colour is not self.colour:
                        moves.append((x - 1, y + 1))

                if y - 1 < 8:
                    figure = chessboard.get_figure_from_position(
                        (x - 1, y - 1))
                    if figure is not None and figure.colour is not self.colour:
                        moves.append((x - 1, y - 1))

            if x is 3:
                figure = chessboard.get_figure_from_position((x, y + 1))
                if isinstance(figure, Pawn) and len(figure.moves) == 1 and (x, y + 1) == chessboard.last_move:
                    moves.append((x - 1, y + 1))

                figure = chessboard.get_figure_from_position((x, y - 1))
                if isinstance(figure, Pawn) and len(figure.moves) == 1 and (x, y - 1) == chessboard.last_move:
                    moves.append((x - 1, y - 1))

        return moves
