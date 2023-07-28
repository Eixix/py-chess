import copy

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
        self.board = [
            [Rook(Colour.WHITE), Knight(Colour.WHITE), Bishop(Colour.WHITE), King(Colour.WHITE), Queen(Colour.WHITE), Bishop(Colour.WHITE), Knight(Colour.WHITE), Rook(Colour.WHITE)],
            [Pawn(Colour.WHITE), Pawn(Colour.WHITE), Pawn(Colour.WHITE), Pawn(Colour.WHITE), Pawn(Colour.WHITE), Pawn(Colour.WHITE), Pawn(Colour.WHITE), Pawn(Colour.WHITE)],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn(Colour.BLACK), Pawn(Colour.BLACK), Pawn(Colour.BLACK), Pawn(Colour.BLACK), Pawn(Colour.BLACK), Pawn(Colour.BLACK), Pawn(Colour.BLACK), Pawn(Colour.BLACK)],
            [Rook(Colour.BLACK), Knight(Colour.BLACK), Bishop(Colour.BLACK), King(Colour.BLACK), Queen(Colour.BLACK), Bishop(Colour.BLACK), Knight(Colour.BLACK), Rook(Colour.BLACK)],
        ]
        self.last_move = ()
        self.whites_turn = True
        self.checked = False

    def check_check(self) -> bool:
        for x, row in enumerate(self.board):
            for y, figure in enumerate(row):
                if figure is not None and figure.colour is (Colour.WHITE if self.whites_turn else Colour.BLACK):
                    for pos in figure.get_moves((x, y), self):
                        king = self.get_figure_from_position(pos)
                        if isinstance(king, King) and king.colour is not figure.colour:
                            self.checked = True
                            return True

        return False

    def check_checkmate(self) -> bool:
        for x, row in enumerate(self.board):
            for y, figure in enumerate(row):
                if figure is not None and figure.colour is (Colour.BLACK if self.whites_turn else Colour.WHITE):
                    for pos in figure.get_moves((x, y), self):
                        clone = copy.deepcopy(self)

                        clone.move_figure((x, y), pos)
                        if not clone.check_check():
                            return False

        return True

    def check_stalemate(self) -> bool:
        for x, row in enumerate(self.board):
            for y, figure in enumerate(row):
                if figure is not None and figure.colour is (Colour.BLACK if self.whites_turn else Colour.WHITE):
                    if len(self.check_possible_moves((x, y))) > 0:
                        return False

        return True

    def check_possible_moves(self, position: tuple[int, int]) -> list[tuple[int, int]]:
        moves = []
        figure = self.get_figure_from_position(position)

        if figure is not None:
            for pos in figure.get_moves(position, self):
                clone = copy.deepcopy(self)
                clone.whites_turn = not clone.whites_turn
                clone.move_figure(position, pos)
                if not clone.check_check():
                    moves.append(pos)

        return moves

    def get_figure_from_position(self, position: tuple[int, int]) -> Figure | None:
        x, y = position

        return self.board[x][y]

    def move_figure(self, start_position: tuple[int, int], end_position: tuple[int, int]) -> None:
        start_x, start_y = start_position
        end_x, end_y = end_position

        figure = self.get_figure_from_position(start_position)

        if isinstance(figure, Pawn) and start_y != end_y and self.get_figure_from_position(end_position) is None:
            self.board[start_x][end_y] = None

        self.board[end_x][end_y] = figure
        self.board[start_x][start_y] = None

        if figure is not None:
            figure.moves.append(end_position)

        if isinstance(figure, King) and abs(start_y - end_y) == 2:
            if end_y < 4:
                self.move_figure((start_x, 0), (start_x, 2))
            else:
                self.move_figure((start_x, 7), (start_x, 4))

        self.last_move = end_position

        if isinstance(figure, Pawn) and ((figure.colour is Colour.WHITE and end_x == 7) or (figure.colour is Colour.BLACK and end_x == 0)):
            queen = Queen(figure.colour)
            queen.moves = figure.moves
            self.board[end_x][end_y] = queen
