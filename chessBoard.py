turns = 0
w = True
board = [["","",""],
         ["","",""],
         ["","",""]]

xOrY = 0

def checkGame():
    #if 3 x or y in a row end game and say winner

    

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


board[1][2] = "1"

print(board)