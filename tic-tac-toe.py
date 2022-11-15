from random import randint

def showTable(boardCreated):
        for row in boardCreated:
            for item in row:
                print(item, end="  ")
            print()

def changeElement(board, row, col, coup):
        board[row][col] = coup

def playerGoingFirst():
    playerStarting = randint(1,2)

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

def ticTactToeStart():
    print("Vous avez démarré une partie de Tic Tac Toe !")
    winJ1 = False
    winJ2 = False
    namePlayer1 = input("Rentrez le nom du J1 : ")
    namePlayer2 = input("Rentrez le nom du J2 : ")
    indexPlayer = playerGoingFirst()
    if indexPlayer == 1 :
        print("Le J1 : " + str(namePlayer1) + " commence !")
        playerFirst = namePlayer1
        playerSecond = namePlayer2
    else:
        print("Le J2 : " + str(namePlayer2) + " commence !")
        playerFirst = namePlayer2
        playerSecond = namePlayer1
    coupPlayerFirst = 'X'
    coupPlayerSecond = 'O'
    print("Début de la partie !")
    print(" ")
    boardGame = [['-','-','-'],['-','-','-'],['-','-','-']]
    showTable(boardGame)
    playerTurn = playerFirst
    coupPlayerTurn = coupPlayerFirst
    while winJ1 == False and winJ2 == False :
        print(" ")
        print("Tour de : ", playerTurn)
        row = int(input("Entrez un numéro de ligne : "))
        col = int(input("Entrez un numéro de colonne : "))
        print(" ")
        changeElement(boardGame,row,col,coupPlayerTurn)
        showTable(boardGame)

        if playerWin(boardGame, coupPlayerTurn):
            print(str(playerFirst) + " a gagné la partie !")
            break

        if boardFilled(boardGame):
            print("Egalité !")
            break 

        if playerTurn == playerFirst :
            playerTurn = playerSecond
            coupPlayerTurn = coupPlayerSecond
        else :
            playerTurn = playerFirst
            coupPlayerTurn = coupPlayerFirst


ticTactToeStart()