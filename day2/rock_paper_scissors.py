from enum import Enum


file = open("day2/input.txt")
lines = file.readlines()
total_score = 0


class Opponent(Enum):
    A = 1
    B = 2
    C = 3


class You(Enum):
    X = 1
    Y = 2
    Z = 3


class Points(Enum):
    WIN = 6
    LOSE = 0
    DRAW = 3


def get_score(opp, you):
    score = 0
    if Opponent[opp].value == You[you].value:
        score = You[you].value+Points.DRAW.value
    elif (opp == 'A' and you == 'Z') or (opp == 'B' and you == 'X') or (opp == 'C' and you == 'Y'):
        score = You[you].value
    else:
        score = You[you].value+Points.WIN.value
    return score


loseDict = {
    # A,X=Rock,B,Y=Paper,C,Z=Scissor
    "A": "Z",
    "B": "X",
    "C": "Y"
}
winDict = {
    # A,X=Rock,B,Y=Paper,C,Z=Scissor
    "A": "Y",
    "B": "Z",
    "C": "X"
}


def cheat(opp, you):
    if you == "X":
        return get_score(opp, loseDict[opp])
    elif you == "Y":
        return get_score(opp, You(Opponent[opp].value).name)
    else:
        return get_score(opp, winDict[opp])


for line in lines:
    total_score += cheat(line[0], line[2])
print(total_score)
