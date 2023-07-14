from typing import Optional
from figures.Figure import Figure
from figures.Pawn import Pawn
from figures.Rook import Rook
from figures.Knight import Knight
from figures.Bishop import Bishop
from figures.Queen import Queen
from figures.King import King
from Colour import Colour


class Chessboard:
    def __init__(self):
        self.board = self._place_figures()

    def get_figure_from_position(self, position: tuple[int, int]) -> Optional[Figure]:
        x, y = position

        return self.board[x][y]

    def move_figure(self, start_position: tuple[int, int], end_position: tuple[int, int]) -> None:
        start_x, start_y = start_position
        end_x, end_y = end_position

        figure = self.get_figure_from_position(start_position)

        if figure is not None and hasattr(figure, 'has_moved'):
            figure.has_moved = True

        self.board[end_x][end_y] = figure
        self.board[start_x][start_y] = None

    def _place_figures(self) -> list[list[Optional[Figure]]]:
        board = [[None for _ in range(8)] for _ in range(8)]

        # White
        for i in range(8):
            board[1][i] = Pawn(Colour.WHITE)

        board[0][0] = Rook(Colour.WHITE)
        board[0][1] = Knight(Colour.WHITE)
        board[0][2] = Bishop(Colour.WHITE)
        board[0][3] = King(Colour.WHITE)
        board[0][4] = Queen(Colour.WHITE)
        board[0][5] = Bishop(Colour.WHITE)
        board[0][6] = Knight(Colour.WHITE)
        board[0][7] = Rook(Colour.WHITE)

        # Black
        for i in range(8):
            board[6][i] = Pawn(Colour.BLACK)

        board[7][0] = Rook(Colour.BLACK)
        board[7][1] = Knight(Colour.BLACK)
        board[7][2] = Bishop(Colour.BLACK)
        board[7][3] = King(Colour.BLACK)
        board[7][4] = Queen(Colour.BLACK)
        board[7][5] = Bishop(Colour.BLACK)
        board[7][6] = Knight(Colour.BLACK)
        board[7][7] = Rook(Colour.BLACK)

        return board
