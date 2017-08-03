import sys
gameBoard = [[1,1,1],[1,1,1],[1,1,1]]

def checkIfGameOver():
    #check row
    for element in gameBoard:
        if('0' not in element and 1 not in element):
            return True
        if ('X' not in element and 1 not in element):
            return True
    return (checkDiagonal(gameBoard, 'X') or checkDiagonal(gameBoard, '0') or checkVertical(gameBoard, 'X') or checkVertical(gameBoard, '0'))


def checkDiagonal(gameBoard, char):
    if(gameBoard[0][0]==char and gameBoard[1][1]==char and gameBoard[2][2]==char):
        return True
    else:
        return False

def checkVertical(gameBoard, char):
    if(gameBoard[0][0]==char and gameBoard[1][0]==char and gameBoard[2][0]==char):
        return True
    if (gameBoard[0][1] == char and gameBoard[1][1] == char and gameBoard[2][1] == char):
        return True
    if (gameBoard[0][2] == char and gameBoard[1][2] == char and gameBoard[2][2] == char):
        return True
    else:
        return False
def isGameDraw():
    for element in gameBoard:
        if (1 in element):
            return False
    return True

def printBoard():
    print gameBoard[0]
    print gameBoard[1]
    print gameBoard[2]

def modifyBoard(row,col,element):
    if(gameBoard[row][col] == 'X' or gameBoard[row][col] == '0'):
        print "Cannot enter " + element + " here this place is full"
        return False
    else:
        gameBoard[row][col] = element
        return True

def play():
    print "Lets play tic tac toe"
    isGameOver = False
    while(not isGameOver):
        p1ModBoard = False
        while (not p1ModBoard):
            p1Row = input(" Player ONE please input row location to put X")
            p1Col = input(" Player ONE please input col location to put X")
            p1ModBoard = modifyBoard(p1Row,p1Col,'X')
            printBoard()
            if(checkIfGameOver()):
                print "Player one wins!"
                return
        p2ModBoard = False
        while(not p2ModBoard):
            p2Row = input(" Player TWO please input row location to put 0")
            p2Col = input(" Player TWO please input col location to put 0")
            p2ModBoard = modifyBoard(p2Row, p2Col, '0')
            printBoard()
            if (checkIfGameOver()):
                print "Player two wins!"
                return
        if(isGameDraw()):
            print "Game drawn!"

def game():
    global gameBoard
    play()
    x = input("Wanna play again ? Enter yes or no")
    if(x=='yes'):
        gameBoard = [[1,1,1],[1,1,1],[1,1,1]]
        game()
    elif(x=='no'):
        sys.exit()
    else:
        print "I did not get that "
        game()
game()