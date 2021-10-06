class Piece:
    def __init__(self, startLocation, colour, icon):
        self.startLocation = startLocation
        self.location = startLocation
        self.colour = colour
        self.icon = icon
        self.hasMoved = False
        self.captured = False

    def __str__(self):
        return self.icon

blackRook = Piece("a1", "black", "♜")
blackRook.location = "a6"

print(blackRook)
print(blackRook.location)