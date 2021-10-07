def board():
    pass

topList = ["♞", "♝", "♟︎", "♟︎", "♟︎", "♟︎", "♝", " ", " ", " ", " ", " ", " ", " ", " ", " "]
botList = ["♘", "♙", "♗", "♘", "♙", "♙", "♙", "♖", " ", " ", " ", " ", " ", " ", " ", " "]
message = '   White Bishop Captured!   '


top = '''     ┌──────────────────┐
     │-{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}-│ 
┌────┴──────────────────┴────┐
│   a  b  c  d  e  f  g  h   │
│ ┌────────────────────────┐ │'''

row8 = "│8│｢ ｣   ｢♗｣   ｢♔｣   ｢ ｣   │ │"
row7 = "│7│   ｢♙｣ ♕ ｢ ｣   ｢ ｣ ♖ ｢ ｣│ │"
row6 = "│6│｢ ｣   ｢ ｣   ｢♙｣   ｢ ｣   │ │"
row5 = "│5│   ｢ ｣   ｢ ｣ ♟︎ ｢♙｣   ｢ ｣│ │"
row4 = "│4│｢ ｣ ♜ ｢ ｣ ♟︎ ｢ ｣ ♟︎ ｢♙｣ ♞ │ │"
row3 = "│3│   ｢ ｣   ｢ ｣   ｢ ｣ ♟︎ ｢ ｣│ │"
row2 = "│2│｢♖｣ ♛ ｢ ｣   ｢ ｣ ♚ ｢ ｣   │ │"
row1 = "│1│   ｢ ｣ ♜ ｢ ｣   ｢ ｣   ｢ ｣│ │"

bot1 = "│ └────────────────────────┘ │"
bot2 = '│{}│'
bot3 = '''└────┬──────────────────┬────┘
     │-{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}-│ ♛d4
     └──────────────────┘'''


print(top.format(*topList))
print(row8)
print(row7)
print(row6)
print(row5)
print(row4)
print(row3)
print(row2)
print(row1)
print(bot1)
print(bot2.format(message))
print(bot3.format(*botList))