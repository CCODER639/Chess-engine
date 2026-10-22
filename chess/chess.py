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


def check(moved,move):
    move = str(move)
    moved = str(moved)
    try:
        if moved[1] == move[1]:
            return "n"
        else:
            return "l"
    except:
        return "l"






while True:
    i = input("enter move: ")
    if i == "y":
        exit()
    p = input("enter the piace you want to use: ")

    convert = "abcdefgh"
    for x in range(len(convert)):
        if convert[x] == i[0]:
            i1 = x
            print(i1)

    for x in range(len(convert)):
        if convert[x] == p[0]:
            p1 = x
            print(p1)


    moved = board[int(p[1])][p1]
    l = check(moved,board[int(i[1])][i1])
    if l == "l":
        board[int(i[1])][i1] = moved
        board[int(p[1])][p1] = 0
    else:
        print("iligal move")

    print(f" a  b  c  d  e  f  g  h  \n{board[0]} 1\n{board[1]} 2\n{board[2]} 3\n{board[3]} 4\n{board[4]} 5\n{board[5]} 6\n{board[6]} 7\n{board[7]} 8\n")
