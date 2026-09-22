
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
        


def movesAndOverlap():
    turns = 0
    w = True
    board = [["","",""],
            ["","",""],
            ["","",""]]

    xOrY = 0
    while w == True:
        if xOrY % 2 == 0:
            move = "x"
        else:
            move = "y"

        x = input("what space do you want: ")
        x1 = int(x[0])
        x2 = int(x[2])
        check = board[x1][x2]
        
        if check == "x" or check == "y":
            print("iligel move try again")
            turns -= 1
            xOrY -= 1
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
            return()
        if game == "y":
            print("y wins")
            return()



movesAndOverlap()