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
    return "g"
        
def csvUp(board,gameSit):
    conversion = {"y": 1, "x": 2, " ": 3, "g": 4}
    board1 = [conversion[item] for row in board for item in row]
    gameSit = conversion[gameSit]
    with open("moves.csv", 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        new_line = board1 + [gameSit]
        csv_writer.writerow(new_line)
     

def movesAndOverlap():
    turns = 0
    w = True
    board = [[" "," "," "],
            [" "," "," "],
            [" "," "," "]]

    xOrY = 0
    while w == True:
        if xOrY % 2 == 0:
            move = "x"
        else:
            move = "y"

        x = int(input("what space do you want 1-9: "))
        x -=1
        x1 = x//3
        x2 = x%3
        check = board[x1][x2]
        
        if check == "x" or check == "y":
            print("iligel move try again")
            
        else:
            board[x1][x2] = move
            
            

            print(board[0])
            print(board[1])
            print(board[2])
            print(turns)
            turns += 1
            xOrY += 1
            
            if turns == 8:
                w = False
            
            game = checkGame(board)
            if game == "x":
                print("x wins")
                csvUp(board,game)
                return()
            if game == "y":
                print("y wins")
                csvUp(board,game)
                return()
            csvUp(board,game)
            



movesAndOverlap()