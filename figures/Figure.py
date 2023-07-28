from typing import TYPE_CHECKING
from Colour import Colour

if TYPE_CHECKING:
    from Chessboard import Chessboard


class Figure:
    def __init__(self, colour: Colour):
        self.colour = colour
        self.moves = []

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {str(self.colour)}"

    def get_picture(self):
        raise NotImplemented()

    def get_moves(self, position: tuple[int, int], chessboard: "Chessboard") -> list[tuple[int, int]]:
        raise NotImplemented()
