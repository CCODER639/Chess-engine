from logic import movesAndOverlap as move
from nm import  hi1


def model(oard):
    board = 0
    while x == True:
        if board == 0:
            conversion = {"x": 1, "y": 2, "": 0, " ": 0}
            board1 = [conversion.get(item, 0) for row in oard for item in row]
            
            board = hi1(board1)
            board3,legal = move(board)
        if legal != "n":
            return board3,legal
        if board < 9:
            board += 1
        elif board == 9:
            board -= 1
            



def human():
    x = True
    while x == True:
        print(1)
        inp = int(input("enter your move 1-9: "))
        board, legal = move(inp)
        if legal != "n":
            return board,legal







t = 0
x = True
while x == True:
    if t % 2 == 1:
        board,l = model(board)

        print(1)

    else:
        board,l = human()

        print(2)

    if l == "x":
        print(l)
        x = False
    elif l == "y":
        print(l)
        x = False

    t += 1
