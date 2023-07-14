from Colour import Colour


class Figure:

    def __init__(self, colour: Colour):
        self.colour = colour

    def __str__(self):
        return f"{self.__class__.__name__} {str(self.colour)}"
