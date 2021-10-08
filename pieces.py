def strToXY(posString):
    return (ord(posString[0].upper()) - 64, int(posString[1]))

def colourReader(colour):
    if colour == "b":
        colourString = "Black"
    if colour == "w":
        colourString = "White"
    return colourString

class Piece:
    def __init__(self, startLocation, colour, icon):
        self.startLocation = self.location = strToXY(startLocation)
        self.colour = colourReader(colour)
        self.icon = icon
        self.hasMoved = False
        self.captured = False
        self.name = self.colour + " " +  self.__class__.__name__

    def __str__(self):
        return self.icon
    
    def canMove(self, dest):
        return False

    def canCapture(self, dest):
        return self.canMove(dest)

class Pawn(Piece):
    def canMove(self, dest):
        output = False
        destXY = strToXY(dest)
        dist = 2
        if self.hasMoved:
            dist = 1

        if destXY != self.location:
            if destXY[0] == self.location[0]:
                if self.colour == "White":
                    output = 0 < destXY[1] - self.location[1] <= dist
                if self.colour == "Black":
                    output = 0 < self.location[1] - destXY[1] <= dist
                
        return output

class King(Piece):
    pass

class Queen(Piece):
    pass

class Bishop(Piece):
    pass

class Knight(Piece):
    pass

class Rook(Piece):
    pass

""" testWhitePawn = Pawn("a2", "w", "♙")
testBlackPawn = Pawn("a7", "b", "♟︎")
testBlackKing = King("e1", "b", "♔")

print(testWhitePawn.canMove("a5"))
print(testBlackPawn.canMove("a6"))
print(testBlackKing.canCapture("f3")) """

""" blackRook = Rook("a1", "b", "♜")
blackRook.location = strToXY("a5")


print(blackRook.name)
print(type(blackRook.startLocation))
print("The black rook is now at: {}.".format(blackRook.location)) """



capturedPieces = {}

whitePieces = {
     
}

blackPieces = {

}

chessPieces = {
    "whitePieces": whitePieces,
    "blackPieces": blackPieces,
    "capturedPieces": capturedPieces
}