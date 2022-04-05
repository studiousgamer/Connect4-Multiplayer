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

def checkConnect4(list):
    for row in list:
        for i in range(len(row) - 1):
            try:
                item = row[i]
                nextItem = row[i + 1]
                nextnextItem = row[i + 2]
                nextnextnextItem = row[i + 3]
                if item == player and nextItem == player and nextnextItem == player and nextnextnextItem == player:
                    return True
            except:
                pass

while True:
    column = int(input("Which column?\n> "))
    if column > 7 or column < 0:
        print("Invalid column")
        break
    os.system("cls")
    grid.reverse()
    for row in grid:
        if row[column - 1] == blank:
            row[column - 1] = player
            break

    grid.reverse()

    columnList = [
        [grid[0][0], grid[1][0], grid[2][0], grid[3][0], grid[4][0], grid[5][0], grid[6][0]],
        [grid[0][1], grid[1][1], grid[2][1], grid[3][1], grid[4][1], grid[5][1], grid[6][1]],
        [grid[0][2], grid[1][2], grid[2][2], grid[3][2], grid[4][2], grid[5][2], grid[6][2]],
        [grid[0][3], grid[1][3], grid[2][3], grid[3][3], grid[4][3], grid[5][3], grid[6][3]],
        [grid[0][4], grid[1][4], grid[2][4], grid[3][4], grid[4][4], grid[5][4], grid[6][4]],
        [grid[0][5], grid[1][5], grid[2][5], grid[3][5], grid[4][5], grid[5][5], grid[6][5]],
        [grid[0][6], grid[1][6], grid[2][6], grid[3][6], grid[4][6], grid[5][6], grid[6][6]]
    ]
    topLeftTobottomRight = [
        [grid[3][0], grid[4][1], grid[5][2], grid[6][3]],
        [grid[2][0], grid[3][1], grid[4][2], grid[5][3], grid[6][4]],
        [grid[1][0], grid[2][1], grid[3][2], grid[4][3], grid[5][4], grid[6][5]],
        [grid[0][0], grid[1][1], grid[2][2], grid[3][3], grid[4][4], grid[5][5], grid[6][6]],
        [grid[0][1], grid[1][2], grid[2][3], grid[3][4], grid[4][5], grid[5][6]],
        [grid[0][2], grid[1][3], grid[2][4], grid[3][5], grid[4][6]],
        [grid[0][3], grid[1][4], grid[2][5], grid[3][6]],
    ]
    topRightTobottomLeft = [
        [grid[0][3], grid[1][2], grid[2][1], grid[3][0]],
        [grid[0][4], grid[1][3], grid[2][2], grid[3][1], grid[4][0]],
        [grid[0][5], grid[1][4], grid[2][3], grid[3][2], grid[4][1], grid[5][0]],
        [grid[0][6], grid[1][5], grid[2][4], grid[3][3], grid[4][2], grid[5][1], grid[6][0]],
        [grid[5][0], grid[4][1], grid[3][2], grid[2][3], grid[1][4], grid[0][5]],
        [grid[4][0], grid[3][1], grid[2][2], grid[1][3], grid[0][4]],
        [grid[3][0], grid[2][1], grid[1][2], grid[0][3]],
    ]

    if checkConnect4(columnList):
        print(f"{player} wins!")
        break
    if checkConnect4(grid):
        print(f"{player} wins!")
        break
    if checkConnect4(topLeftTobottomRight):
        print(f"{player} wins!")
        break
    if checkConnect4(topRightTobottomLeft):
        print(f"{player} wins!")
        break

    player = "O" if player == "X" else "X"
    for row in grid:
        print(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]}")
