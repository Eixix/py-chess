import copy

from Colour import Colour
from figures.Bishop import Bishop
from figures.Figure import Figure
from figures.King import King
from figures.Knight import Knight
from figures.Pawn import Pawn
from figures.Queen import Queen
from figures.Rook import Rook


def _place_figures() -> list[list[Figure | None]]:
    return [
        [Rook(Colour.WHITE), Knight(Colour.WHITE), Bishop(Colour.WHITE), King(Colour.WHITE), Queen(Colour.WHITE),
         Bishop(Colour.WHITE), Knight(Colour.WHITE), Rook(Colour.WHITE)],
        [Pawn(Colour.WHITE), Pawn(Colour.WHITE), Pawn(Colour.WHITE), Pawn(Colour.WHITE), Pawn(Colour.WHITE),
         Pawn(Colour.WHITE), Pawn(Colour.WHITE), Pawn(Colour.WHITE)],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [Pawn(Colour.BLACK), Pawn(Colour.BLACK), Pawn(Colour.BLACK), Pawn(Colour.BLACK), Pawn(Colour.BLACK),
         Pawn(Colour.BLACK), Pawn(Colour.BLACK), Pawn(Colour.BLACK)],
        [Rook(Colour.BLACK), Knight(Colour.BLACK), Bishop(Colour.BLACK), King(Colour.BLACK), Queen(Colour.BLACK),
         Bishop(Colour.BLACK), Knight(Colour.BLACK), Rook(Colour.BLACK)],
    ]


class Chessboard:
    def __init__(self):
        self.board: list[list[Figure | None]] = _place_figures()
        self.whites_turn = True
        self.last_move = ()
        self.checked = False

    def get_figure_from_position(self, position: tuple[int, int]) -> Figure | None:
        x, y = position
        return self.board[x][y]

    def _promote(self, figure: Pawn, pos_x: int, pos_y: int):
        queen = Queen(figure.colour)
        queen.moves = figure.moves
        self.board[pos_x][pos_y] = queen

    def check_check(self) -> bool:
        for x, row in enumerate(self.board):
            for y, figure in enumerate(row):
                if figure is not None and figure.colour == (Colour.WHITE if self.whites_turn else Colour.BLACK):
                    for position in figure.get_moves((x, y), self):
                        possible_king = self.get_figure_from_position(position)
                        if isinstance(possible_king, King) and possible_king.colour != figure.colour:
                            self.checked = True
                            return True
        return False

    def check_checkmate(self) -> bool:
        for x, row in enumerate(self.board):
            for y, figure in enumerate(row):
                if figure is not None and figure.colour == (Colour.BLACK if self.whites_turn else Colour.WHITE):
                    for position in figure.get_moves((x, y), self):
                        clone = copy.deepcopy(self)
                        clone.move_figure((x, y), position)
                        if not clone.check_check():
                            return False
        return True

    def check_stalemate(self) -> bool:
        for x, row in enumerate(self.board):
            for y, figure in enumerate(row):
                if figure is not None and figure.colour == (Colour.BLACK if self.whites_turn else Colour.WHITE):
                    if len(self.check_possible_moves_for_piece((x, y))) > 0:
                        return False
        return True

    def check_possible_moves_for_piece(self, start_position: tuple[int, int]) -> list[tuple[int, int]]:
        moves = []
        figure = self.get_figure_from_position(start_position)
        for end_position in figure.get_moves(start_position, self):
            clone = copy.deepcopy(self)
            clone.whites_turn = not clone.whites_turn
            clone.move_figure(start_position, end_position)
            if not clone.check_check():
                moves.append(end_position)
        return moves

    def move_figure(self, start_position: tuple[int, int], end_position: tuple[int, int]):
        start_x, start_y = start_position
        end_x, end_y = end_position
        figure = self.get_figure_from_position(start_position)

        # En passant
        if isinstance(figure, Pawn) and start_y != end_y and self.get_figure_from_position(end_position) is None:
            self.board[start_x][end_y] = None

        self.board[end_x][end_y] = figure
        self.board[start_x][start_y] = None

        # Castling
        if isinstance(figure, King) and abs(start_y - end_y) == 2:
            if end_y < 4:
                self.move_figure((start_x, 0), (start_x, 2))
            else:
                self.move_figure((start_x, 7), (start_x, 4))

        # Save moves to figure
        figure.moves.append(end_position)
        self.last_move = end_position

        # Promotion (defaulted to Queen)
        if isinstance(figure, Pawn) and ((figure.colour == Colour.WHITE and end_x == 7) or (
                figure.colour == Colour.BLACK and end_x == 0)):
            self._promote(figure, end_x, end_y)
