# 0 = black ,1 = pawn ,2 = king, 3= queen, 4 = bishop , 5 = knight , 6 = rook
        # a b c d e f g h   1 = black 0 = white
board = [[61,51,41,21,31,41,51,61],#0
         [11,11,11,11,11,11,11,11],#1
         [0,0,0,0,0,0,0,0],#2
         [0,0,0,0,0,0,0,0],#3
         [0,0,0,0,0,0,0,0],#4
         [0,0,0,0,0,0,0,0],#5
         [10,10,10,10,10,10,10,10],#6
         [60,50,40,20,30,40,50,60]]#7


def check(moved,move,p2,p1,i2,i1):
    print(p2,i2,9)
    
    move = str(move)
    moved = str(moved)
    
    try:
        if moved[1] == move[1]:
            return "n"
    except:
        pass
    
    if moved[0] == "1":
        
        if p2 +1 != i2:
            print(p2,i2)
            return "n"
  
        print("hi")
        if p2 == 1:
            print("hi")
            if p2 +2 != i2:
                print(2)
                return "n"
    return("l")
        
            
            
    
    





print(f" a  b  c  d  e  f  g  h  \n{board[0]} 0\n{board[1]} 1\n{board[2]} 2\n{board[3]} 3\n{board[4]} 4\n{board[5]} 5\n{board[6]} 6\n{board[7]} 7\n")
while True:
    i = input("enter move: ")
    if i == "y":
        exit()
    p = input("enter the piace you want to use: ")

    convert = "abcdefgh"
    
    i2 = int(i[1])
    p2 = int(p[1])
    for x in range(len(convert)):
        if convert[x] == i[0]:
            i1 = x
            print(i1)

    for x in range(len(convert)):
        if convert[x] == p[0]:
            p1 = x
            print(p1)


    moved = board[p2][p1]
    l = check(moved,board[i2][i1],p2,p1,i2,i1)
    if l == "l":
        board[i2][i1] = moved
        board[p2][p1] = 0
    else:
        print("iligal move")

    print(f" a  b  c  d  e  f  g  h  \n{board[0]} 0\n{board[1]} 1\n{board[2]} 2\n{board[3]} 3\n{board[4]} 4\n{board[5]} 5\n{board[6]} 6\n{board[7]} 7\n")
    

