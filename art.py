boardDict = {
"whiteCapList": [" ", " ", " ", " ", " ", " ", " ", " ",
          " ", " ", " ", " ", " ", " ", " ", " "],
"blackCapList": [" ", " ", " ", " ", " ", " ", " ", " ",
          " ", " ", " ", " ", " ", " ", " ", " "],
"row8List": [" ", " ", " ", " ", " ", " ", " ", " "],
"row7List": [" ", " ", " ", " ", " ", " ", " ", " "],
"row6List": [" ", " ", " ", " ", " ", " ", " ", " "],
"row5List": [" ", " ", " ", " ", " ", " ", " ", " "],
"row4List": [" ", " ", " ", " ", " ", " ", " ", " "],
"row3List": [" ", " ", " ", " ", " ", " ", " ", " "],
"row2List": [" ", " ", " ", " ", " ", " ", " ", " "],
"row1List": [" ", " ", " ", " ", " ", " ", " ", " "],
"message": '                            ', # 28 characters

"top": '''     ┌──────────────────┐
     │-{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}-│
┌────┴──────────────────┴────┐
│   a  b  c  d  e  f  g  h   │
│ ┌────────────────────────┐ │''',

"row8": "│8│｢{}｣ {} ｢{}｣ {} ｢{}｣ {} ｢{}｣ {} │ │",
"row7": "│7│ {} ｢{}｣ {} ｢{}｣ {} ｢{}｣ {} ｢{}｣│ │",
"row6": "│6│｢{}｣ {} ｢{}｣ {} ｢{}｣ {} ｢{}｣ {} │ │",
"row5": "│5│ {} ｢{}｣ {} ｢{}｣ {} ｢{}｣ {} ｢{}｣│ │",
"row4": "│4│｢{}｣ {} ｢{}｣ {} ｢{}｣ {} ｢{}｣ {} │ │",
"row3": "│3│ {} ｢{}｣ {} ｢{}｣ {} ｢{}｣ {} ｢{}｣│ │",
"row2": "│2│｢{}｣ {} ｢{}｣ {} ｢{}｣ {} ｢{}｣ {} │ │",
"row1": "│1│ {} ｢{}｣ {} ｢{}｣ {} ｢{}｣ {} ｢{}｣│ │",

"bot1": "│ └────────────────────────┘ │",
"bot2": '│{}│',
"bot3": '''└────┬──────────────────┬────┘
     │-{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}-│
     └──────────────────┘'''
}

def printBoard(piecesDict):
     
     whiteCaptured = 0
     blackCaptured = 0

     for chessPiece in piecesDict["capturedPieces"].keys():
          piece = piecesDict["capturedPieces"][chessPiece]
          if piece.colour == "White":
               boardDict["whiteCapList"][whiteCaptured] = piece.icon
               whiteCaptured += 1
          if piece.colour == "Black":
               boardDict["blackCapList"][blackCaptured] = piece.icon
               blackCaptured += 1

     for chessPiece in piecesDict["whitePieces"].keys():
          piece = piecesDict["whitePieces"][chessPiece]
          loc = piece.location
          col = loc[0] - 1
          row = boardDict["row"+ str(loc[1]) +"List"]
          row[col] = piece.icon

     for chessPiece in piecesDict["blackPieces"].keys():
          piece = piecesDict["blackPieces"][chessPiece]
          loc = piece.location
          col = loc[0] - 1
          row = boardDict["row"+ str(loc[1]) +"List"]
          row[col] = piece.icon


     print(boardDict["top"].format(*boardDict["whiteCapList"]))
     print(boardDict["row8"].format(*boardDict["row8List"]))
     print(boardDict["row7"].format(*boardDict["row7List"]))
     print(boardDict["row6"].format(*boardDict["row6List"]))
     print(boardDict["row5"].format(*boardDict["row5List"]))
     print(boardDict["row4"].format(*boardDict["row4List"]))
     print(boardDict["row3"].format(*boardDict["row3List"]))
     print(boardDict["row2"].format(*boardDict["row2List"]))
     print(boardDict["row1"].format(*boardDict["row1List"]))
     print(boardDict["bot1"])
     print(boardDict["bot2"].format(boardDict["message"]))
     print(boardDict["bot3"].format(*boardDict["blackCapList"]))