import csv



def checkGame(board):
    #if 3 x or y in a row end game and say winner
    
    for xOrY in ["x","y"]:
        for attempt in range(3):
            if board[attempt][0] == xOrY and board[attempt][1] == xOrY and board[attempt][2] == xOrY:
                return(xOrY)

            if board[0][attempt] == xOrY and board[1][attempt] == xOrY and board[2][attempt] == xOrY:
                return(xOrY)
            
        if board[0][0] == xOrY and board[2][2] == xOrY and board[1][1] == xOrY :
            return(xOrY)
        if board[2][0] == xOrY and board[0][2] == xOrY and board[1][1] == xOrY :
            return(xOrY)

def csvUp(board, gameSit):
    conversion = {"y": 1, "x": 2, "": 0, "l": 4, "n": 0, "g": 4}
    board1 = [conversion.get(item, 0) for row in board for item in row]
    gameVal = conversion.get(gameSit, 0)

    with open("moves.csv", 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(board1 + [gameVal])
 

turns = 0
w = True
board = [["","",""],
        ["","",""],
        ["","",""]]

xOrY = 0

def movesAndOverlap(x):
    global turns
    global w
    global board
    global xOrY
    
    if xOrY % 2 == 0:
        move = "x"
    else:
        move = "y"

    x -= 1
    x1 = x//3
    x2 = x%3
    check = board[x1][x2]
    
    if check == "x" or check == "y":
        print("iligel move try again")
        turns -= 1
        xOrY -= 1
        return(board,"n")
    else:
        board[x1][x2] = move

    print(board[0])
    print(board[1])
    print(board[2])
    print(turns)
    turns +=1
    if turns == 8:
        w = False
    xOrY += 1
    game = checkGame(board)
    if game == "x":
        print("x wins")
        csvUp(board,game)
        return(board,"x")
    elif game == "y":
        print("y wins")
        csvUp(board,game)
        return(board,"y")
    else:
        csvUp(board, "l")
        return(board, "l")




