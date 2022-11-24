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

# on déini une fonction canWinTest() avec comme arguments a, b, c qui sont 3 éléments de notre tableau de jeu et player le coup du joueur/ elle teste si sur les 3 éléments deux sont remplis avec le meme signe et si le dernier est vide, elle renvoie True ou False si la condition est vérifier et l'emplacement manquant pour gagné   
def canWinTest(a, b, c, player):
    # si le premier élément a et le deuxieme element b sont egaux au coup du joueur et que le troisieme element c est vide
    if a == b == player and c == '-':
        # alors
        # on retourne True et l'index 2 qui correspond a l'élément c vide
        return[True, 2]
    # si le troisieme element c et le premier élément a sont egaux au coup du joueur et que le deuxieme element b est vide
    elif c == a == player and b == '-':
        # alors
        # on retourne True et l'index 1 qui correspond a l'élément b vide
        return[True, 1]
    # si le deuxieme element b et le troisieme element c sont egaux au coup du joueur et que le  premier élément a est vide
    elif b == c == player and a == '-':
        # alors
        # on retourne True et l'index 0 qui correspond a l'élément a vide
        return[True, 0]
    # sinon
    else:
        # on retourne False
        return[False]

# on défini une fonction canWin() avec comme arguments board qui est notre plateau de jeu, et player le coup du joueur / elle teste si sur toutes les lignes et diagonales si le coup donné en argument peut gagner, si oui elle renvoie True plus l'emplacement x, y de la case pouvant faire gagner le joueur sinon elle renvoie une liste vide 
def canWin(board, player):
    # on créer une boucle for qui se repete avec i allant de 0 a 1 a 2
    for i in range(3):
        # on donne a la variable ligne la valeur du renvoie de la fonction canWinTest() allant de [i][0] a [i][2]
        ligne = canWinTest(board[i][0], board[i][1], board[i][2], player)
        # si ligne[0] ( soit Win ou False ) est égale a True 
        if ligne[0] == True:
            # alors
            # on retourne i, et ligne [1] qui sont les coordonnés de la case manquante pour gagner 
            return i, ligne[1]
        # on donne a la variable colonne la valeur du renvoie de la fonction canWinTest() allant de [0][i] a [2][i]
        colone = canWinTest(board[0][i], board[1][i], board[2][i], player)
        # si colone[0] ( soit Win ou False ) est égale a True 
        if colone[0] == True:
            # alors
            # on retourne colonne[1], i qui sont les coordonnés de la case manquante pour gagner 
            return colone[1], i
    # on donne a la variable diagoUn la valeur du renvoie de la fonction canWinTest()
    diagoUn = canWinTest(board[0][0], board[1][1], board[2][2], player)
    # on donne a la variable diagoDeux la valeur du renvoie de la fonction canWinTest()
    diagoDeux = canWinTest(board[0][2], board[1][1], board[2][0], player)
    # si diagoUn[0] ( soit Win ou False ) est égale a True 
    if diagoUn[0] == True:
        # alors
        # on retourne diagoUn[1] et diagoUn[1]
        return diagoUn[1], diagoUn[1]
    # si diagoDeux[0] ( soit Win ou False ) est égale a True 
    if diagoDeux[0] == True:
        # alors
        # on retourne diagoDeux[1] et 2-diagoDeux[1]
        return diagoDeux[1], 2-diagoDeux[1]
    # sinon
    # on retourne une liste vide 
    return []

def iaPlay(board, iacoup, player, turn, coupAlreadyMade):
    # premier tour
    # si turn == 1
    if turn == 1:
            # si on joue milieu 
            if board[1][1] == player:
                # alors l'ia joue coin 
                coupAlreadyMade.append([2,0]) 
                return changeElement(board, 2, 0, iacoup)
            # si autre
            else:
                # alors l'ia joue milieu
                coupAlreadyMade.append([1,1]) 
                return changeElement(board, 1, 1, iacoup)
           
    # deuxième tour
    # si turn == 2
    if turn == 2:
            # si on a joue milieu
            if board[1][1] == player:
                # si on joue toute les cases qui peuvent nous faire gagner 
                if canWin(board,player) != []:  # a [x,x]
                    # l'ia bloque la dernière case 
                    coupAlreadyMade.append([canWin(board,player)[0],canWin(board,player)[1]])  
                    return changeElement(board, canWin(board,player)[0], canWin(board,player)[1], iacoup)
                # si on joue la case qui s'aligne avec le coup de l'ia 
                if canWin(board,player) == []:
                    # l'ia joue le coin case opposé pour créer une ligne avec un coup au milieu manquant
                    if board[2][0] == iacoup:
                        coupAlreadyMade.append([0,0]) 
                        return changeElement(board, 0, 0, iacoup)
                
            # si on a joue coin 
            if board[0][0] == player or board[0][2] == player or board[2][0] == player or board[2][2] == player :
                # si on joue une case qui aligne deux de nos coups
                if canWin(board,player) != []:  # a [x,x]
                    # l'ia le bloque
                    coupAlreadyMade.append([canWin(board,player)[0],canWin(board,player)[1]])
                    return changeElement(board, canWin(board,player)[0], canWin(board,player)[1], iacoup)
                # si on joue un coup qui n'aligne pas deux de nos coups
                if canWin(board,player) == []:
                    # l'ia aligne son deuxieme coup avec son premier et un espace vide
                    if board[0][0] == player and board[2][2] == player or board[0][2] == player and board[2][0] == player :
                        coupAlreadyMade.append([1,0]) 
                        return changeElement(board, 1, 0, iacoup)
                    else:
                        if board[0][0] == player and board[2][1] == player:
                            coupAlreadyMade.append([1, 2]) 
                            return changeElement(board, 1, 2, iacoup)
                        if board[0][0] == player and board[1][2] == player:
                            coupAlreadyMade.append([2, 1]) 
                            return changeElement(board, 2, 1, iacoup)
                        if board[0][2] == player and board[2][1] == player:
                            coupAlreadyMade.append([1, 0]) 
                            return changeElement(board, 1, 0, iacoup)
                        if board[0][2] == player and board[1][0] == player:
                            coupAlreadyMade.append([2, 1]) 
                            return changeElement(board, 2, 1, iacoup)
                        if board[2][0] == player and board[0][1] == player:
                            coupAlreadyMade.append([1, 2]) 
                            return changeElement(board, 1, 2, iacoup)
                        if board[2][0] == player and board[1][2] == player:
                            coupAlreadyMade.append([0, 1]) 
                            return changeElement(board, 0, 1, iacoup)
                        if board[2][2] == player and board[1][0] == player:
                            coupAlreadyMade.append([0, 1]) 
                            return changeElement(board, 0, 1, iacoup)
                        if board[2][2] == player and board[0][1] == player:
                            coupAlreadyMade.append([1, 0]) 
                            return changeElement(board, 1, 0, iacoup)
    # troisieme tour et quatrième
    # si turn == 3 ou 4
    if turn == 3 or turn == 4:
        # si possibilité de gagner == True 
        if canWin(board,iacoup) != []:  # a [x,x]
            # gagner 
            coupAlreadyMade.append([canWin(board,player)[0],canWin(board,player)[1]])
            return changeElement(board, canWin(board,iacoup)[0], canWin(board,iacoup)[1], iacoup)
        # si joueur possibilité de gagner == True
        if canWin(board,player) != []:  # a [x,x]
            # bloquer 
            coupAlreadyMade.append([canWin(board,player)[0],canWin(board,player)[1]])
            return changeElement(board, canWin(board,player)[0], canWin(board,player)[1], iacoup)
        # sinon 
        if canWin(board,player) == [] and  canWin(board,iacoup) == []: 
            # jouer pour aligner / remplir
            for l in range(3):
                for r in range(3):
                    if [l,r] not in coupAlreadyMade :
                        coupAlreadyMade.append([l,r])
                        return changeElement(board, l, r, iacoup)


# on déini une fonction ticTactToeStart() avec comme arguments namePlayer1, scoreJ1 défini comme égale a 0 et scoreJ1 défini comme égale a 0 / elle contient notre jeu
def ticTactToeStart(namePlayer1, scoreJ1 = 0, scoreJ2 = 0):
    # on met notre variable coupAlreadyMade en global
    global coupAlreadyMade
    # on affiche "Vous avez démarré une partie de Tic Tac Toe !"
    print("Vous avez démarré une partie de Tic Tac Toe !")
    # ! affichage ésthétique ! 
    print(" ")
    # on attribut la valeur de False a la variable winJ1
    winJ1 = False
    # on attribut la valeur de False a la variable winJ2
    winJ2 = False
    # on attribut la valeur de la variable namePlayer1 a la variable playerFirst
    playerFirst = namePlayer1
    # on attribut la valeur de la chaine de caractere "IA" a la variable namePlayer2
    namePlayer2 = "IA"
    # on attribut la valeur de la variable namePlayer2 a la variable playerSecond
    playerSecond = namePlayer2
    # on attribut la valeur de la chaine de caractere "X" a la variable coupPlayerFirst
    coupPlayerFirst = 'X'
    # on attribut la valeur de la chaine de caractere "O" a la variable coupPlayerSecond
    coupPlayerSecond = 'O'
    # on affiche "Début de la partie !"
    print("Début de la partie !")
    turn = 1
    # ! affichage ésthétique ! 
    print(" ")
    boardGame = [['-','-','-'],['-','-','-'],['-','-','-']]
    showBoardGame(boardGame)
    # ! affichage ésthétique ! 
    print(" ")
    playerTurn = playerFirst
    coupPlayerTurn = coupPlayerFirst
    coupAlreadyMade = []
    while winJ1 == False or winJ2 == False :
        print("Tour de : ", playerTurn)
        print("Coup actuel : ", coupPlayerTurn)
        if playerTurn == namePlayer1:
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
                        break  
                # ! affichage ésthétique !              
                print(" ")
                try :
                    changeElement(boardGame,row,col,coupPlayerTurn)
                    break
                except IndexError :
                    print("Coup non valide rentrez un nombre entre 0 et 2")
                    # ! affichage ésthétique ! 
                    print(" ")
            showBoardGame(boardGame)
            # ! affichage ésthétique ! 
            print(" ")

        elif playerSecond == namePlayer2:
            iaPlay(boardGame, coupPlayerSecond, coupPlayerFirst, turn, coupAlreadyMade) 
            turn += 1  
            # ! affichage ésthétique ! 
            print(" ")
            showBoardGame(boardGame)
            # ! affichage ésthétique ! 
            print(" ")

        if playerWin(boardGame, coupPlayerTurn):
            print(str(playerTurn) + " a gagné la partie !")
            if playerTurn == namePlayer1 : 
                scoreJ1 += 1   
            else :               
                scoreJ2 += 1
            # ! affichage ésthétique ! 
            print(" ")
            break

        if boardFilled(boardGame):  
            print("Egalité !")     
            # ! affichage ésthétique ! 
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
        # ! affichage ésthétique ! 
        print(" ")
        ticTactToeStart(namePlayer1, scoreJ1, scoreJ2 )

    else:
        # ! affichage ésthétique ! 
        print(" ")
        print("Score final de " + str(namePlayer1) + " : " + str(scoreJ1))
        print("Score final de " + str(namePlayer2) + " : " + str(scoreJ2))
        # ! affichage ésthétique ! 
        print(" ")
        print("Fin du jeu !")
        # ! affichage ésthétique ! 
        print(" ")

ticTactToeStart("Gabriel")