from typing import TYPE_CHECKING
from figures.Figure import Figure
from Colour import Colour

if TYPE_CHECKING:
    from Chessboard import Chessboard


class Bishop(Figure):
    def __init__(self, colour: Colour):
        super().__init__(colour)

    def get_picture(self):
        return '♗' if self.colour is Colour.WHITE else '♝'

    def get_moves(self, position: tuple[int, int], chessboard: "Chessboard") -> list[tuple[int, int]]:
        moves = []
        x, y = position

        # Top Right
        tmp_x = x
        tmp_y = y
        while tmp_x + 1 < 8 and tmp_y + 1 < 8:
            pos = (tmp_x + 1, tmp_y + 1)
            figure = chessboard.get_figure_from_position(pos)

            if figure is None:
                moves.append(pos)
            elif figure.colour is not self.colour:
                moves.append(pos)
                break
            else:
                break

            tmp_x += 1
            tmp_y += 1

        # Bottom Right
        tmp_x = x
        tmp_y = y
        while tmp_x - 1 >= 0 and tmp_y + 1 < 8:
            pos = (tmp_x - 1, tmp_y + 1)
            figure = chessboard.get_figure_from_position(pos)

            if figure is None:
                moves.append(pos)
            elif figure.colour is not self.colour:
                moves.append(pos)
                break
            else:
                break

            tmp_x -= 1
            tmp_y += 1

        # Bottom Left
        tmp_x = x
        tmp_y = y
        while tmp_x - 1 >= 0 and tmp_y - 1 >= 0:
            pos = (tmp_x - 1, tmp_y - 1)
            figure = chessboard.get_figure_from_position(pos)

            if figure is None:
                moves.append(pos)
            elif figure.colour is not self.colour:
                moves.append(pos)
                break
            else:
                break

            tmp_x -= 1
            tmp_y -= 1

        # Top Left
        tmp_x = x
        tmp_y = y
        while tmp_x + 1 < 8 and tmp_y - 1 >= 0:
            pos = (tmp_x + 1, tmp_y - 1)
            figure = chessboard.get_figure_from_position(pos)

            if figure is None:
                moves.append(pos)
            elif figure.colour is not self.colour:
                moves.append(pos)
                break
            else:
                break

            tmp_x += 1
            tmp_y -= 1

        return moves
