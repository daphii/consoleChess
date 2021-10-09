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
        self.pieceType = self.__class__.__name__
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



whitePieces = {
    "whiteKing": King('e1', 'w', '♚'),
    "whiteQueen": Queen('d1', 'w', '♛'),
    "whiteBishop1": Bishop('c1', 'w', '♝'),
    "whiteBishop2": Bishop('f1', 'w', '♝'),
    "whiteKnight1": Knight('b1', 'w', '♞'),
    "whiteKnight2": Knight('g1', 'w', '♞'),
    "whiteRook1": Rook('a1', 'w', '♜'),
    "whiteRook2": Rook('h1', 'w', '♜'),
    "whitePawn1": Pawn('a2', 'w', '♟'),
    "whitePawn2": Pawn('b2', 'w', '♟'),
    "whitePawn3": Pawn('c2', 'w', '♟'),
    "whitePawn4": Pawn('d2', 'w', '♟'),
    "whitePawn5": Pawn('e2', 'w', '♟'),
    "whitePawn6": Pawn('f2', 'w', '♟'),
    "whitePawn7": Pawn('g2', 'w', '♟'),
    "whitePawn8": Pawn('h2', 'w', '♟')   
}

blackPieces = {
    "blackKing": King('e8', 'b', '♔'),
    "blackQueen": Queen('d8', 'b', '♕'),
    "blackBishop1": Bishop('c8', 'b', '♗'),
    "blackBishop2": Bishop('f8', 'b', '♗'),
    "blackKnight1": Knight('b8', 'b', '♘'),
    "blackKnight2": Knight('g8', 'b', '♘'),
    "blackRook1": Rook('a8', 'b', '♖'),
    "blackRook2": Rook('h8', 'b', '♖'),
    "blackPawn1": Pawn('a7', 'b', '♙'),
    "blackPawn2": Pawn('b7', 'b', '♙'),
    "blackPawn3": Pawn('c7', 'b', '♙'),
    "blackPawn4": Pawn('d7', 'b', '♙'),
    "blackPawn5": Pawn('e7', 'b', '♙'),
    "blackPawn6": Pawn('f7', 'b', '♙'),
    "blackPawn7": Pawn('g7', 'b', '♙'),
    "blackPawn8": Pawn('h7', 'b', '♙')
}

capturedPieces = {
}

chessPieces = {
    "whitePieces": whitePieces,
    "blackPieces": blackPieces,
    "capturedPieces": capturedPieces
}