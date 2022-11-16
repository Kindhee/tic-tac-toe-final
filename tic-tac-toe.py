# DEBUT

# on importe la fonction randint de la librairie random 
from random import randint

# on déini une fonction showBoardGame() avec comme argument boardCreated qui est le plateau de jeu créer
def showBoardGame(boardCreated):
    # on créer une boucle for qui parcours toutes les lignes de notre plateau
        for row in boardCreated:
            # on créer une boucle for qui parcours tout les éléments de notre plateau
            for item in row:
                # on affiche chaque élément avec deux espace a la fin grace a end = "  "
                print(item, end="  ")
            # on affiche avec un retour a la ligne après chaque ligne de 3 éléments 
            print()

# on déini une fonction changeElement() avec comme arguments board qui est notre plateau de jeu, row les lignes du plateau, col les colonnes du plateau et coup le coup ( soit "X" soit "O" )
def changeElement(board, row, col, coup):
        # on change la valeur de notre plateau avec un index de ligne et de colonne par le coup du joueur 
        board[row][col] = coup

# on déini une fonction playerGoingFirst() sans argument
def playerGoingFirst():
    # on retourne un nombre aléatoire entre 1 et 2 avec randint(1, 2)
    return randint(1,2)

# on déini une fonction playerWin() avec comme arguments board qui est notre plateau de jeu et player le coup du joueur ( soit "X" soit "O" )
def playerWin(board, player):
    # on donne la valeur de None a une varibale win
    win = None
    # on donne la valeur de len(board) a une varibale n
    n = len(board)
    # on créer une boucle for qui parcours tout les index i des éléments de notre plateau
    for i in range(n):
        # on donne la valeur de True a la varibale win
        win = True
        # on créer une boucle for qui parcours tout les index j des éléments de notre plateau 
        for j in range(n):
            # on créer une condition if qui teste si notre plateau a un index de ligne et de colonne donné est différent de player
            if board[i][j] != player:
                # alors 
                # on donne la valeur de False a la varibale win
                win = False
                # on utilise un break pour sortir des boucles 
                break
        # on créer une condition if qui teste si win est égale a True 
        if win:
            # alors
            # on retourne win
            return win

    # on créer une boucle for qui parcours tout les index i des éléments de notre plateau
    for i in range(n):
        # on donne la valeur de True a la varibale win
        win = True
        # on créer une boucle for qui parcours tout les index j des éléments de notre plateau 
        for j in range(n):
            # on créer une condition if qui teste si notre plateau a un index de ligne et de colonne donné est différent de player
            if board[j][i] != player:
                # alors 
                # on donne la valeur de False a la varibale win
                win = False
                # on utilise un break pour sortir des boucles 
                break
         # on créer une condition if qui teste si win est égale a True 
        if win:
            # alors
            # on retourne win
            return win

    # on donne la valeur de True a la varibale win
    win = True
    # on créer une boucle for qui parcours tout les index i des éléments de notre plateau
    for i in range(n):
        # on créer une condition if qui teste si notre plateau a un index de ligne et de colonne donné est différent de player
        if board[i][i] != player:
                # alors 
                # on donne la valeur de False a la varibale win
                win = False
                # on utilise un break pour sortir des boucles 
                break
    # on créer une condition if qui teste si win est égale a True 
    if win:
        # alors
        # on retourne win
        return win

    # on donne la valeur de True a la varibale win
    win = True
    # on créer une boucle for qui parcours tout les index i des éléments de notre plateau
    for i in range(n):
        # on créer une condition if qui teste si notre plateau a un index de i et n - 1 - i est différent de player
        if board[i][n - 1 - i] != player:
            # alors 
            # on donne la valeur de False a la varibale win
            win = False
            # on utilise un break pour sortir des boucles 
            break
    # on créer une condition if qui teste si win est égale a True 
    if win:
        # alors
        # on retourne win
        return win
    # sinon on retourne False
    return False

# on déini une fonction boardFilled() avec comme argument board qui est notre plateau de jeu
def boardFilled(board):
    # on créer une boucle for qui parcours toutes les lignes de notre plateau
    for row in board:
        # on créer une boucle for qui parcours tout les éléments de notre plateau
        for item in row:
            # on créer une condition if qui teste si un éléments donné est égale a '-' 
            if item == '-':
                # alors
                # on retourne False
                return False
    # sinon on retourne True
    return True

# on déini une fonction ticTactToeStart() avec comme arguments namePlayer1, namePlayer2, scoreJ1 défini comme égale a 0 et scoreJ1 défini comme égale a 0
def ticTactToeStart(namePlayer1, namePlayer2, scoreJ1 = 0, scoreJ2 = 0):
    # on affiche "Vous avez démarré une partie de Tic Tac Toe !"
    print("Vous avez démarré une partie de Tic Tac Toe !")
    # ! affichage purement esthétique !
    print(" ")
    # on donne la valeur de False a une varibale winJ1
    winJ1 = False
    # on donne la valeur de False a une varibale winJ2
    winJ2 = False
    # on donne la valeur retournée par la fonction playerGoingFirst() a une varibale indexPlayer
    indexPlayer = playerGoingFirst()
    # on créer une condition if qui teste si indexPlayer est égale a 1
    if indexPlayer == 1 :
        # alors
        # on affiche "Le J1 : (nom du joueur 1 ) commence !"
        print("Le J1 : " + str(namePlayer1) + " commence !")
        # on donne la chaine de caractères namePlayer1 a la variable playerFirst
        playerFirst = namePlayer1
        # on donne la chaine de caractères namePlayer2 a la variable playerSecond
        playerSecond = namePlayer2
    # on créer une condition elif qui teste sinon si indexPlayer est égale a 2 
    elif indexPlayer == 2 :
        # on affiche # on affiche "Le J2 : (nom du joueur 2 ) commence !"
        print("Le J2 : " + str(namePlayer2) + " commence !")
        # on donne la chaine de caractères namePlayer2 a la variable playerFirst
        playerFirst = namePlayer2
        # on donne la chaine de caractères namePlayer1 a la variable playerSecond
        playerSecond = namePlayer1
    coupPlayerFirst = 'X'
    coupPlayerSecond = 'O'
    # on affiche ""
    print("Début de la partie !")
    # ! affichage purement esthétique !
    print(" ")
    boardGame = [['-','-','-'],['-','-','-'],['-','-','-']]
    showBoardGame(boardGame)
    # ! affichage purement esthétique !
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
                # on affiche ""
                print("Entrez un numéro de ligne : ")
                row = int(input(" > "))
                # on affiche ""
                print("Entrez un numéro de colonne : ")
                col = int(input(" > "))
                if not([row,col] in coupAlreadyMade):
                    coupAlreadyMade.append([row,col])
                    coupAvailable = True
                    validationTest = True
            # ! affichage purement esthétique !
            print(" ")
            try :
                changeElement(boardGame,row,col,coupPlayerTurn)
                break
            except IndexError :
                # on affiche ""
                print("Coup non valide rentrez un nombre entre 0 et 2")
                # ! affichage purement esthétique !
                print(" ")
        showBoardGame(boardGame)
        # ! affichage purement esthétique !
        print(" ")

        if playerWin(boardGame, coupPlayerTurn):
            # on affiche ""
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
    
    # on affiche ""
    print("Rejouez ? ( y ) yes ou ( n ) no ")
    replay = input(" > ")
    if replay == "y":
        # on affiche ""
        print("Score de " + str(namePlayer1) + " : " + str(scoreJ1))
        # on affiche ""
        print("Score de " + str(namePlayer2) + " : " + str(scoreJ2))
        # ! affichage purement esthétique !
        print(" ")
        ticTactToeStart(namePlayer1, namePlayer2, scoreJ1, scoreJ2 )
    else:
        # ! affichage purement esthétique !
        print(" ")
        # on affiche ""
        print("Score final de " + str(namePlayer1) + " : " + str(scoreJ1))
        # on affiche ""
        print("Score final de " + str(namePlayer2) + " : " + str(scoreJ2))
        # ! affichage purement esthétique !
        print(" ")
        # on affiche ""
        print("Fin du jeu !")
        # ! affichage purement esthétique !
        print(" ")

# on appel notre fonction ticTactToeStart() avec en arguments les noms des deux joueurs en str ("...", "...")
ticTactToeStart("Romain", "Gabriel")

# FIN