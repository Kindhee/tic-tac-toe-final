from random import randint

def showBoardGame(boardCreated):
        for row in boardCreated:
            for item in row:
                print(item, end="  ")
            print()

def changeElement(board, row, col, coup):
        board[row][col] = coup

def playerGoingFirst():
    return randint(1,2)

def playerWin(board, player):
    win = None
    n = len(board)
    for i in range(n):
        win = True
        for j in range(n):
            if board[i][j] != player:
                win = False
                break
        if win:
            return win

    for i in range(n):
        win = True
        for j in range(n):
            if board[j][i] != player:
                win = False
                break
        if win:
            return win

    win = True
    for i in range(n):
        if board[i][i] != player:
            win = False
            break
    if win:
        return win

    win = True
    for i in range(n):
        if board[i][n - 1 - i] != player:
            win = False
            break
    if win:
        return win
    return False

def boardFilled(board):
    for row in board:
        for item in row:
            if item == '-':
                return False
    return True

def ticTactToeStart(namePlayer1, namePlayer2, scoreJ1 = 0, scoreJ2 = 0):
    print("Vous avez démarré une partie de Tic Tac Toe !")
    print(" ")
    winJ1 = False
    winJ2 = False
    indexPlayer = playerGoingFirst()
    if indexPlayer == 1 :
        print("Le J1 : " + str(namePlayer1) + " commence !")
        playerFirst = namePlayer1
        playerSecond = namePlayer2
    elif indexPlayer == 2 :
        print("Le J2 : " + str(namePlayer2) + " commence !")
        playerFirst = namePlayer2
        playerSecond = namePlayer1
    coupPlayerFirst = 'X'
    coupPlayerSecond = 'O'
    print("Début de la partie !")
    print(" ")
    boardGame = [['-','-','-'],['-','-','-'],['-','-','-']]
    showBoardGame(boardGame)
    print(" ")
    playerTurn = playerFirst
    coupPlayerTurn = coupPlayerFirst
    coupAlreadyMade = []
    while winJ1 == False and winJ2 == False :
        # print("AAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ")
        print("Tour de : ", playerTurn)
        coupAvailable = False
        validationTest = False
        while coupAvailable == False:
            while validationTest == False : 
                print("Entrez un numéro de ligne : ")
                row = int(input(" > "))
                print("Entrez un numéro de colonne : ")
                col = int(input(" > "))
                if not([row,col] in coupAlreadyMade):
                    coupAlreadyMade.append([row,col])
                    coupAvailable = True
                    validationTest = True
            print(" ")
            try :
                changeElement(boardGame,row,col,coupPlayerTurn)
                break
            except IndexError :
                print("Coup non valide rentrez un nombre entre 0 et 2")
                print(" ")
        showBoardGame(boardGame)
        print(" ")

        if playerWin(boardGame, coupPlayerTurn):
            print(str(playerTurn) + " a gagné la partie !")
            if playerTurn == namePlayer1 :
                scoreJ1 += 1
            else :
                scoreJ2 += 1
            print(" ")
            break

        if boardFilled(boardGame):
            print("Egalité !")
            print(" ")
            break 

        if playerTurn == playerFirst :
            playerTurn = playerSecond
            coupPlayerTurn = coupPlayerSecond
        else :
            playerTurn = playerFirst
            coupPlayerTurn = coupPlayerFirst

    print("Rejouez ? ( y ) yes ou ( n ) no ")
    replay = input(" > ")
    if replay == "y":
        print("Score de " + str(namePlayer1) + " : " + str(scoreJ1))
        print("Score de " + str(namePlayer2) + " : " + str(scoreJ2))
        print(" ")
        ticTactToeStart(namePlayer1, namePlayer2, scoreJ1, scoreJ2 )
    else:
        print(" ")
        print("Score final de " + str(namePlayer1) + " : " + str(scoreJ1))
        print("Score final de " + str(namePlayer2) + " : " + str(scoreJ2))
        print(" ")
        print("Fin du jeu !")
        print(" ")

ticTactToeStart("Romain", "Gabriel")