from typing import TYPE_CHECKING

from Colour import Colour
from figures.Figure import Figure

if TYPE_CHECKING:
    from Chessboard import Chessboard


class Pawn(Figure):

    def __init__(self, colour: Colour):
        super().__init__(colour)

    def get_picture(self):
        return "♙" if self.colour == Colour.WHITE else "♟︎"

    def get_moves(self, position: tuple[int, int], chessboard: "Chessboard") -> list[tuple[int, int]]:
        moves = []
        x, y = position

        if self.colour == Colour.WHITE:
            if x + 1 < 8 and (chessboard.get_figure_from_position((x + 1, y))) is None:
                moves.append((x + 1, y))
                if not self.moves and chessboard.get_figure_from_position((x + 2, y)) is None:
                    moves.append((x + 2, y))
            if x + 1 < 8:
                if y + 1 < 8 and chessboard.get_figure_from_position(
                        (x + 1, y + 1)) is not None and chessboard.get_figure_from_position(
                    (x + 1, y + 1)).colour != self.colour:
                    moves.append((x + 1, y + 1))
                if y - 1 >= 0 and chessboard.get_figure_from_position(
                        (x + 1, y - 1)) is not None and chessboard.get_figure_from_position(
                    (x + 1, y - 1)).colour != self.colour:
                    moves.append((x + 1, y - 1))
            # En passant
            if x == 4:
                if isinstance(chessboard.get_figure_from_position((x, y + 1)), Pawn) and len(
                        chessboard.get_figure_from_position((x, y + 1)).moves) == 1 and chessboard.last_move == (
                        x, y + 1):
                    moves.append((x + 1, y + 1))
                if isinstance(chessboard.get_figure_from_position((x, y - 1)), Pawn) and len(
                        chessboard.get_figure_from_position((x, y - 1)).moves) == 1 and chessboard.last_move == (
                        x, y - 1):
                    moves.append((x + 1, y - 1))
        else:
            if x - 1 >= 0 and (chessboard.get_figure_from_position((x - 1, y))) is None:
                moves.append((x - 1, y))
                if not self.moves and chessboard.get_figure_from_position((x - 2, y)) is None:
                    moves.append((x - 2, y))
            if x - 1 >= 0:
                if y + 1 < 8 and chessboard.get_figure_from_position(
                        (x - 1, y + 1)) is not None and chessboard.get_figure_from_position(
                    (x - 1, y + 1)).colour != self.colour:
                    moves.append((x - 1, y + 1))
                if y - 1 >= 0 and chessboard.get_figure_from_position(
                        (x - 1, y - 1)) is not None and chessboard.get_figure_from_position(
                    (x - 1, y - 1)).colour != self.colour:
                    moves.append((x - 1, y - 1))
            if x == 3:
                if isinstance(chessboard.get_figure_from_position((x, y + 1)), Pawn) and len(
                        chessboard.get_figure_from_position((x, y + 1)).moves) == 1 and chessboard.last_move == (
                        x, y + 1):
                    moves.append((x - 1, y + 1))
                if isinstance(chessboard.get_figure_from_position((x, y - 1)), Pawn) and len(
                        chessboard.get_figure_from_position((x, y - 1)).moves) == 1 and chessboard.last_move == (
                        x, y - 1):
                    moves.append((x - 1, y - 1))

        return moves
