# DEBUT

# on importe la fonction randint de la librairie random 
from random import randint

# on déini une fonction showBoardGame() avec comme argument boardCreated qui est le plateau de jeu créer / elle sert a afficher le tableau de jeu
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

# on déini une fonction playerGoingFirst() sans argument / elle renvoie un nombre aléatoire entre 1 et 2 pour choisir un joueur aléatoirement
def playerGoingFirst():
    # on retourne un nombre aléatoire entre 1 et 2 avec randint(1, 2)
    return randint(1,2)

# on déini une fonction playerWin() avec comme arguments board qui est notre plateau de jeu et player le coup du joueur ( soit "X" soit "O" ) / elle teste si un des deux joueur a gagné 
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

# on déini une fonction boardFilled() avec comme argument board qui est notre plateau de jeu / elle teste si le plateau de jeu est remplis
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

# on déini une fonction ticTactToeStart() avec comme arguments namePlayer1, namePlayer2, scoreJ1 défini comme égale a 0 et scoreJ1 défini comme égale a 0 / elle contient notre jeu
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
        # on affiche "Le J1 : (nom du joueur 1) commence !"
        print("Le J1 : " + str(namePlayer1) + " commence !")
        # on donne la chaine de caractères namePlayer1 a la variable playerFirst
        playerFirst = namePlayer1
        # on donne la chaine de caractères namePlayer2 a la variable playerSecond
        playerSecond = namePlayer2
    # on créer une condition elif qui teste sinon si indexPlayer est égale a 2 
    elif indexPlayer == 2 :
        # on affiche # on affiche "Le J2 : (nom du joueur 2) commence !"
        print("Le J2 : " + str(namePlayer2) + " commence !")
        # on donne la chaine de caractères namePlayer2 a la variable playerFirst
        playerFirst = namePlayer2
        # on donne la chaine de caractères namePlayer1 a la variable playerSecond
        playerSecond = namePlayer1
    # on donne la chaine de caractères 'X' a la variable coupPlayerFirst
    coupPlayerFirst = 'X'
    # on donne la chaine de caractères 'O' a la variable coupPlayerSecond
    coupPlayerSecond = 'O'
    # on affiche "Début de la partie !"
    print("Début de la partie !")
    # ! affichage purement esthétique !
    print(" ")
    # on donne une liste de 3 listes avec chacune 3 éléments '-' a la variable boardGame
    boardGame = [['-','-','-'],['-','-','-'],['-','-','-']]
    # on appelle notre fonction showBoardGame() avec en argument notre plateau de jeu boardGame
    showBoardGame(boardGame)
    # ! affichage purement esthétique !
    print(" ")
    # on donne comme valeur playerFirst a notre variable playerTurn
    playerTurn = playerFirst
    # on donne comme valeur coupPlayerFirst a notre variable coupPlayerTurn
    coupPlayerTurn = coupPlayerFirst
    # on défini une liste vide coupAlreadyMade
    coupAlreadyMade = []
    # on créer une boucle while qui se répète tant que winJ1 ou winJ2 sont égale a False
    while winJ1 == False or winJ2 == False :
        # on affiche "Tour de : (nom joueur jouant a ce tour)"
        print("Tour de : ", playerTurn)
        # on donne la valeur de False a la variable coupAvailable
        coupAvailable = False
        # on donne la valeur de False a la variable validationTest
        validationTest = False
        # on créer une boucle while qui se répète tant que coupAvailable est égale a False      
        while coupAvailable == False:
            # on créer une boucle while qui se répète tant que validationTest est égale a False
            while validationTest == False : 
                # on affiche "Entrez un numéro de ligne : "
                print("Entrez un numéro de ligne : ")
                # on demande un input en int dans la variable row qui sera le numéro de ligne
                row = int(input(" > "))
                # on affiche "Entrez un numéro de colonne : "
                print("Entrez un numéro de colonne : ")
                # on demande un input en int dans la variable col qui sera le numéro de colonne
                col = int(input(" > "))
                # on créer une condition if qui teste si [row,col] n'est pas déjâ dans la liste coupAlreadyMade
                if not([row,col] in coupAlreadyMade):
                    # alors
                    # on ajoute [row,col] dans notre liste coupAlreadyMade
                    coupAlreadyMade.append([row,col])
                    # on change la valeur de coupAvailable a True
                    coupAvailable = True
                    # on change la valeur de validationTest a True
                    validationTest = True
            # ! affichage purement esthétique !
            print(" ")
            # on teste
            try :
                # on appelle la fonction changeElement avec comme arguments boardGame notre plateau de jeu, row notre numéro de ligne, col notre numéro de colonne et coupPlayerTurn son coup soit 'X' soit 'O'
                changeElement(boardGame,row,col,coupPlayerTurn)
                # on quitte la boucle
                break
            # si l'erreur IndexError est renvoyé 
            except IndexError :
                # on affiche "Coup non valide rentrez un nombre entre 0 et 2"
                print("Coup non valide rentrez un nombre entre 0 et 2")
                # ! affichage purement esthétique !
                print(" ")
        # on appelle notre fonction showBoardGame() avec en argument notre plateau de jeu boardGame
        showBoardGame(boardGame)
        # ! affichage purement esthétique !
        print(" ")

        # on créer une condition if qui teste si la fonction playerWin() avec comme argmuments boardGame notre plateau de jeu, coupPlayerTurn son coup soit 'X' soit 'O', renvoie True
        if playerWin(boardGame, coupPlayerTurn):
            # alors
            # on affiche "(nom joueur jouant a ce tour) a gagné la partie !"
            print(str(playerTurn) + " a gagné la partie !")
            # on créer une condition if qui teste si la variable playerTurn est égale a la variable namePlayer1
            if playerTurn == namePlayer1 :
                # alors
                # on incrémente la variable scoreJ1 de + 1 
                scoreJ1 += 1
            # sinon 
            else :
                # on incrémente la variable scoreJ2 de + 1 
                scoreJ2 += 1
            # ! affichage purement esthétique !
            print(" ")
            # on quitte la boucle
            break
        
        # on créer une condition if qui teste si la fonction boardFilled() avec comme argument boardGame notre plateau de jeu renvoie True
        if boardFilled(boardGame):
            # on affiche "Egalité !"
            print("Egalité !")
            # ! affichage purement esthétique !
            print(" ")
            # on quitte la boucle
            break 
        
        # on créer une condition if qui teste si la variable playerTurn est égale a la variable playerFirst
        if playerTurn == playerFirst :
            # alors
            # la variable playerTurn est égale a la valeur de la variable playerSecond
            playerTurn = playerSecond
            # la variable coupPlayerTurn est égale a la valeur de la variable coupPlayerSecond
            coupPlayerTurn = coupPlayerSecond
        # sinon
        else :
            # la variable playerTurn est égale a la valeur de la variable playerFirst
            playerTurn = playerFirst
            # la variable coupPlayerTurn est égale a la valeur de la variable coupPlayerFirst
            coupPlayerTurn = coupPlayerFirst
    
    # on affiche "Rejouez ? ( y ) yes ou ( n ) no "
    print("Rejouez ? ( y ) yes ou ( n ) no ")
    # on donne la valeur d'un input en str a une variable replay
    replay = input(" > ")

    # on créer une condition if qui teste si la variable replay est égale a "y"
    if replay == "y":
        # alors 
        # on affiche "Score de (nom du joueur 1) : (score du joueur 1)"
        print("Score de " + str(namePlayer1) + " : " + str(scoreJ1))
        # on affiche "Score de (nom du joueur 2) : (score du joueur 2)"
        print("Score de " + str(namePlayer2) + " : " + str(scoreJ2))
        # ! affichage purement esthétique !
        print(" ")
        #on appelle notre fonction ticTactToeStart() de manière récursive avec comme arguments namePlayer1 le nome du joueur 1, namePlayer2 le nome du joueur 2, scoreJ1 le score du joueur 1 et scoreJ2 le score du joueur 2 
        ticTactToeStart(namePlayer1, namePlayer2, scoreJ1, scoreJ2 )
    # sinon
    else:
        # ! affichage purement esthétique !
        print(" ")
        # on affiche "Score final de (nom du joueur 1) : (score du joueur 1)"
        print("Score final de " + str(namePlayer1) + " : " + str(scoreJ1))
        # on affiche "Score final de (nom du joueur 2) : (score du joueur 2)"
        print("Score final de " + str(namePlayer2) + " : " + str(scoreJ2))
        # ! affichage purement esthétique !
        print(" ")
        # on affiche "Fin du jeu !"
        print("Fin du jeu !")
        # ! affichage purement esthétique !
        print(" ")

# on appel notre fonction ticTactToeStart() avec en arguments les noms des deux joueurs en str ("nom joueur 1", "nom joueur 2")
ticTactToeStart("Romain", "Gabriel")

# FIN