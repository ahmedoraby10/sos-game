arr1=["null","null","null","null","null","null","null","null",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,"null","null","null","null","null","null","null","null"]
arr2=["null","null","null","null","null","null","null","null",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,"null","null","null","null","null","null","null","null"]
score1=0
score2=0
def board():
    print(" |  ", arr1[8]," | ",arr1[9]," | ",arr1[10]," | ",arr1[11],"  | ")
    print(" |  ", arr1[12]," | ",arr1[13]," | ",arr1[14]," | ",arr1[15],"  | ")
    print(" |  ", arr1[16]," | ","{0:>2}".format(arr1[17]),"| ", "{0:>2}".format(arr1[18]),"| ", "{0:>2}".format(arr1[19])," | ")
    print(" |  ", "{0:>2}".format(arr1[20]),"| ", "{0:>2}".format(arr1[21]),"| ", "{0:>2}".format(arr1[22]),"| ","{0:>2}".format(arr1[23])," |  " )
    print("player1","player2")
    print("  ", score1,"    ",score2)

def player1():
    plays = ["s","o"]
    print("player 1's turn!")
    play = str(input("chose a letter(s , o)"))
    if play not in plays:
        print("invaled move!")
        player1()
    else:
        move = moves(play)
        check_points1(play,move)

def player2():
    plays = ["s", "o"]
    print("player 2's turn!")
    play = str(input("chose a letter(s , o)"))
    if play not in plays:
        print("invaled move!")
        player2()
    else:
        move = moves(play)
        check_points2(play, move)


def moves(m):
    move = int(input("enter a number from 1 to 16"))
    if (move) not in arr1:
        print("invalid move!")
        moves(m)
    else:
        arr1[move + 7]= m
        arr2[move + 7]= "null"
        return (move + 7)


def game_process():
    while True:
        board()
        player1()
        if arr2.count(arr2[0]) == len(arr2):
            board()
            if score1 > score2:
                print("player one wins!")
                break
            elif score2 > score1:
                print("player two wins!")
                break
            elif score1 == score2:
                print("Draw!")
                break
        board()
        player2()
        if arr2.count(arr2[0]) == len(arr2):
            board()
            if score1 > score2:
                print("player one wins!")
                break
            elif score2>score1:
                print("player two wins!")
                break
            elif score1 == score2:
                print("Draw!")
                break

def check_points1(m,n):
    global score1
    invalid1=[8,12,16,20,11,15,19,23]
    invalid2=[8,12,16,20,9,13,17,21]
    invalid3=[11,15,19,23,10,14,18,22]
    if m == "o":
        if n in invalid1:
            if (arr1[n - 4])== "s" and arr1[n + 4]=="s":
                score1 +=1
                board()
                player1()
        elif (arr1[n - 1]== "s" and arr1[ n + 1]== "s") or (arr1[n - 4]== "s" and arr1[n + 4]== "s") or (arr1[n - 3]== "s" and arr1[n + 3]== "s") or (arr1[n - 5]== "s" and arr1[n + 5]== "s"):
                score1 +=1
                board()
                player1()
    elif m == "s":
        if n in invalid2:
            if (arr1[n + 1]== "o" and arr1[n + 2]== "s" ) or (arr1[n + 4]== "o" and arr1[n + 8]== "s" ) or (arr1[n - 4]== "o" and arr1[n - 8]== "s" ) or (arr1[n - 3]== "o" and arr1[n - 6]== "s" ) or (arr1[n + 5]== "o" and arr1[n + 10]== "s" ):
                    score1 +=1
                    board()
                    player1()
        elif n in invalid3:
            if (arr1[n - 1]== "o" and arr1[n - 2]== "s") or (arr1[n + 4]== "o" and arr1[n + 8]== "s") or (arr1[n - 4]== "o" and arr1[n - 8]== "s") or (arr1[n + 3]== "o" and arr1[n + 6]== "s") or (arr1[n - 5]== "o" and arr1[n - 10]== "s"):
                    score1 +=1
                    board()
                    player1()

def check_points2(m,n):
    global score2
    invalid1 = [8, 12, 16, 20, 11, 15, 19, 23]
    invalid2 = [8, 12, 16, 20, 9, 13, 17, 21]
    invalid3 = [11, 15, 19, 23, 10, 14, 18, 22]
    if m == "o":
        if n in invalid1:
            if (arr1[n - 4])== "s" and arr1[n + 4]=="s":
                score2 +=1
                board()
                player2()
        elif (arr1[n - 1]== "s" and arr1[ n + 1]== "s") or (arr1[n - 4]== "s" and arr1[n + 4]== "s") or (arr1[n - 3]== "s" and arr1[n + 3]== "s") or (arr1[n - 5]== "s" and arr1[n + 5]== "s"):
                score2 +=1
                board()
                player2()
    elif m == "s":
        if n in invalid2:
            if (arr1[n + 1]== "o" and arr1[n + 2]== "s" ) or (arr1[n + 4]== "o" and arr1[n + 8]== "s" ) or (arr1[n - 4]== "o" and arr1[n - 8]== "s" ) or (arr1[n - 3]== "o" and arr1[n - 6]== "s" ) or (arr1[n + 5]== "o" and arr1[n + 10]== "s" ):
                    score2 +=1
                    board()
                    player2()
        elif n in invalid3:
            if (arr1[n - 1]== "o" and arr1[n - 2]== "s") or (arr1[n + 4]== "o" and arr1[n + 8]== "s") or (arr1[n - 4]== "o" and arr1[n - 8]== "s") or (arr1[n + 3]== "o" and arr1[n + 6]== "s") or (arr1[n - 5]== "o" and arr1[n - 10]== "s"):
                    score2 +=1
                    board()
                    player2()
game_process()











