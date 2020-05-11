import random
from datetime import datetime
#    x0  x1  x2
# y0 0 | 1 | 2
# y1 3 | 4 | 5
# y2 6 | 7 | 8

gameEnded = False
winner = None

gameData = [
    [-1, -1, -1],
    [-1, -1, -1],
    [-1, -1, -1]
]
freeSpace = gameData


def draw():
    out = ""

    for v in gameData:
        i = 0
        for k in v:
            i = i + 1
            if k == -1:
                if i == 3:
                    out = out + " |\n"
                else:
                    out = out + " |"
            else:
                what = "O"

                if k == 0:
                    what = "O"
                elif k == 1:
                    what = "X"
                else:
                    what = ""

                if i == 3:
                    out = out + "{w}|\n".format(w=what)
                else:
                    out = out + "{w}|".format(w=what)

    print(out)


def checkHorizontalWin(y, x, winChar):
    if x == 0:
        if gameData[y][x] == winChar and gameData[y][x+1] == winChar and gameData[y][x+2] == winChar:
            return True
        else:
            return False
    elif x == 1:
        if gameData[y][x-1] == winChar and gameData[y][x] == winChar and gameData[y][x+1] == winChar:
            return True
        else:
            return False
    elif x == 2:
        if gameData[y][x-2] == winChar and gameData[y][x-1] == winChar and gameData[y][x] == winChar:
            return True
        else:
            return False


def checkDiagonalWin(y, x, winChar):
    if x == 0:
        if y == 0:
            if gameData[y][x] == winChar and gameData[y+1][x+1] == winChar and gameData[y+2][x+2] == winChar:
                return True
            else:
                return False
        elif y == 2:
            if gameData[y][x] == winChar and gameData[y-1][x+1] == winChar and gameData[y-2][x-2] == winChar:
                return True
            else:
                return False
    elif x == 1:
        if y == 1:
            if gameData[y-1][x-1] == winChar and gameData[y][x] == winChar and gameData[y+1][x+1] == winChar:
                return True
            elif gameData[y+1][x-1] == winChar and gameData[y][x] == winChar and gameData[y-1][x+1] == winChar:
                return True
            else:
                return False
    elif x == 2:
        if y == 0:
            if gameData[y][x] == winChar and gameData[y+1][x-1] == winChar and gameData[y+2][x-2] == winChar:
                return True
            else:
                return False
        elif y == 2:
            if gameData[y][x] == winChar and gameData[y-1][x-1] == winChar and gameData[y-2][x-2] == winChar:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def checkVerticalWin(y, x, winChar):
    if x == 0:
        if y == 0:
            if gameData[y][x] == winChar and gameData[y+1][x] == winChar and gameData[y+2][x] == winChar:
                return True
            else:
                return False
        elif y == 1:
            if gameData[y-1][x] == winChar and gameData[y][x] == winChar and gameData[y+1][x] == winChar:
                return True
            else:
                return False
        elif y == 2:
            if gameData[y - 2][x] == winChar and gameData[y - 1][x] == winChar and gameData[y][x] == winChar:
                return True
            else:
                return False
        else:
            return False
    elif x == 1:
        if y == 0:
            if gameData[y][x] == winChar and gameData[y + 1][x] == winChar and gameData[y + 2][x] == winChar:
                return True
            else:
                return False
        elif y == 1:
            if gameData[y - 1][x] == winChar and gameData[y][x] == winChar and gameData[y + 1][x] == winChar:
                return True
            else:
                return False
        elif y == 2:
            if gameData[y - 2][x] == winChar and gameData[y - 1][x] == winChar and gameData[y][x] == winChar:
                return True
            else:
                return False
        else:
            return False
    elif x == 2:
        if y == 0:
            if gameData[y][x] == winChar and gameData[y + 1][x] == winChar and gameData[y + 2][x] == winChar:
                return True
            else:
                return False
        elif y == 1:
            if gameData[y - 1][x] == winChar and gameData[y][x] == winChar and gameData[y + 1][x] == winChar:
                return True
            else:
                return False
        elif y == 2:
            if gameData[y - 2][x] == winChar and gameData[y - 1][x] == winChar and gameData[y][x] == winChar:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def won(char):
    tempWinner = "¯\\_(ツ)_/¯"
    # Check for horizontal wins
    for y in range(0, 3):
        for x in range(0, 3):
            # y0, x0 | y0, x1 | y0, x2
            # y1, x0 | y1, x1 | y0, x2
            # y2, x0 | y2, x1 | y2, x2

            if checkDiagonalWin(y, x, char) or checkVerticalWin(y, x, char) or checkHorizontalWin(y, x, char):
                if char == 1:
                    tempWinner = "Player"
                elif char == 0:
                    tempWinner = "\"AI\""
                else:
                    tempWinner = "¯\\_(ツ)_/¯"
                break

    if tempWinner == "¯\\_(ツ)_/¯":
        return "-1.{p}".format(p=tempWinner)
    else:
        return "{c}.{p}".format(c=char, p=tempWinner)


def ai():
    random.seed(datetime.now())
    x = random.randint(0, 2)
    y = random.randint(0, 2)

    while True:
        if gameData[y][x] == -1:
            break
        else:
            x = random.randint(0, 2)
            y = random.randint(0, 2)

    if gameData[y][x] == -1:
        freeSpace[y][x] = 0
        gameData[y][x] = 0


def plrInput():
    yourChoice = input("Which area would you like to choose?")

    try:
        yourChoice = int(yourChoice)
    except ValueError:
        print("You dumfuk")

    if isinstance(yourChoice, int):
        if 6 <= yourChoice < 9:
            if gameData[0][yourChoice - 6] == -1:
                gameData[2][yourChoice - 6] = 1
                freeSpace[2][yourChoice - 6] = 1
            else:
                print("Area ({x},{y}) taken, choose another area.".format(x=yourChoice - 6, y=2))
                plrInput()
        elif 3 <= yourChoice < 6:
            if gameData[0][yourChoice - 3] == -1:
                gameData[1][yourChoice - 3] = 1
                freeSpace[1][yourChoice - 3] = 1
            else:
                print("Area ({x},{y}) taken, choose another area.".format(x=yourChoice - 3, y=1))
                plrInput()
        elif -1 < yourChoice < 3:
            if gameData[0][yourChoice] == -1:
                gameData[0][yourChoice] = 1
                freeSpace[0][yourChoice] = 1
            else:
                print("Area ({x},{y}) taken, choose another area.".format(x=yourChoice, y=0))
                plrInput()


def main():
    global gameEnded
    global winner

    if not gameEnded:
        draw()
        plrInput()
        draw()

        ai()
        draw()

        playerWon = won(1) or False
        enemyWon = won(0) or False

        tempStr = playerWon.split(".")

        if tempStr[0] != "-1":
            winner = tempStr[1]
            print("{w} won the game!".format(w=winner))
            gameEnded = True
        else:
            tempStr = enemyWon.split(".")

            if tempStr[0] != "-1":
                winner = tempStr[1]
                print("{w} won the game!".format(w=winner))
                gameEnded = True

        main()


main()
