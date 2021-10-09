from art import printBoard
from pieces import chessPieces

""" for dictionary in chessPieces.keys():
    print()
    for piece in chessPieces[dictionary].keys():
        chessPiece = chessPieces[dictionary][piece]
        print("{} {} -> {} starts at {}".format(chessPiece.colour, chessPiece.pieceType, chessPiece.icon, chessPiece.startLocation))
 """

printBoard(chessPieces)