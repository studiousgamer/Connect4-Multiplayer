import os

blank = " "
grid = [
    [blank, blank, blank, blank, blank, blank, blank],
    [blank, blank, blank, blank, blank, blank, blank],
    [blank, blank, blank, blank, blank, blank, blank],
    [blank, blank, blank, blank, blank, blank, blank],
    [blank, blank, blank, blank, blank, blank, blank],
    [blank, blank, blank, blank, blank, blank, blank],
    [blank, blank, blank, blank, blank, blank, blank]
]
player = "X"

while True:
    column = int(input("Which column?\n> "))
    dropRow = ""
    os.system("cls")
    grid.reverse()
    for row in grid:
        if row[column - 1] == blank:
            row[column - 1] = player
            dropRow = row
            break
    
    grid.reverse()
    
    if player == "X":
        player = "O"
    else:
        player = "X"

    for row in grid:
        print(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]}")
