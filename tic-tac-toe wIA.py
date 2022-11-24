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

# on défini une fonction iaPlay() avec comme arguments board qui est notre plateau de jeu, iaCoup le coup de l'ia, player le coup du joueur, turn le tour actuel et coupAlreadyMade les coups deja pris dans le tableau  / cette fonction permet de faire jouer notre ia
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
                    # sinon
                    else:
                        # conditions pratiques pour s'aligner le mieux possible en fonction des deux coups exact du joueur
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
    # on attribut la valeur de 1 a la variable turn
    turn = 1
    # ! affichage ésthétique ! 
    print(" ")
    # on créer une liste de 3 listes contenant chacune trois élément '-' dans notre variable boardGame
    boardGame = [['-','-','-'],['-','-','-'],['-','-','-']]
    # on affiche la variable boardGame a l'aide de la fonction showBoard(), cela affiche notre tableau de jeu
    showBoardGame(boardGame)
    # ! affichage ésthétique ! 
    print(" ")
    # on attribut la valeur de la variable playerFirst a la variable playerTurn
    playerTurn = playerFirst
    # on attribut la valeur de la variable coupPlayerFirst a la variable coupPlayerTurn
    coupPlayerTurn = coupPlayerFirst
    # on défini une variable coupAlreadyMade qui est une liste vide
    coupAlreadyMade = []
    # on créer une boucle while qui se répete tant que winJ1 et winJ2 sont égale a False
    while winJ1 == False or winJ2 == False :
        # on affiche "Tour de : ( nom du joueur jouant )"
        print("Tour de : ", playerTurn)
        # on affiche "Coup actuel : ( coup du joueur jouant )"
        print("Coup actuel : ", coupPlayerTurn)
        # si playerTurn est égal a namePlayer1
        if playerTurn == namePlayer1:
            # alors
            # on met la variable coupAvailable a False
            coupAvailable = False
            # on met la variable validationTest a False
            validationTest = False
            # on créer une boucle while qui se répete tant que coupAvailable est égal a False
            while coupAvailable == False:
                # on créer une boucle while qui se répete tant que validationTest est égal a False
                while validationTest == False : 
                    # on affiche "Entrez un numéro de ligne : "
                    print("Entrez un numéro de ligne : ")     
                    # on assigne a la variable row la valeur donné suite a un input du joueur             
                    row = int(input(" > "))      
                    # on affiche "Entrez un numéro de colonne : "
                    print("Entrez un numéro de colonne : ") 
                    # on assigne a la variable col la valeur donné suite a un input du joueur                  
                    col = int(input(" > "))                   
                    # si notre couple [row,col] n'est pas dans notre liste coupAlreadyMade
                    if not([row,col] in coupAlreadyMade):                                 
                        # alors
                        # on ajoute [row,col] a notre liste coupAlreadyMade             
                        coupAlreadyMade.append([row,col])                  
                        # on sort de la boucle   
                        break  
                # ! affichage ésthétique !              
                print(" ")
                # on essaie avec try
                try :
                    # on appel la fonction changeElement() avec en commentaire boardGame qui est notre plateau de jeu, row le numéro de ligne, col le numéro de colonne et coupPlayerTurn le coup du joueur qui joue ce tour
                    changeElement(boardGame,row,col,coupPlayerTurn)
                    # on sort de la boucle 
                    break
                # si l'erreur IndexEroor nous es renvoyé 
                except IndexError :
                    # alors 
                    # on affiche "Coup non valide rentrez un nombre entre 0 et 2"
                    print("Coup non valide rentrez un nombre entre 0 et 2")
                    # ! affichage ésthétique ! 
                    print(" ")
            
            # on affiche la variable boardGame a l'aide de la fonction showBoard(), cela affiche notre tableau de jeu
            showBoardGame(boardGame)
            # ! affichage ésthétique ! 
            print(" ")

        # sinon si playerSecond est égal a namePlayer2
        elif playerSecond == namePlayer2:
            # on appelle notre fonction iaPlay() avec comme arguments boardGame notre plateau de jeu, coupPlayerSecond le coup du J2, coupPlayerFirst le coup du J1, turn le tour actuel et coupAlreadyMade les coups déja faits sur le plateau
            iaPlay(boardGame, coupPlayerSecond, coupPlayerFirst, turn, coupAlreadyMade) 
            # on ajoute +1 la variable turn
            turn += 1  
            # ! affichage ésthétique ! 
            print(" ")
            # on affiche la variable boardGame a l'aide de la fonction showBoard(), cela affiche notre tableau de jeu
            showBoardGame(boardGame)
            # ! affichage ésthétique ! 
            print(" ")

        # si la fonction playerWin() renvoie True 
        if playerWin(boardGame, coupPlayerTurn):
            # alors
            # on affiche "(nom du joueur gagnant) a gagné la partie !"
            print(str(playerTurn) + " a gagné la partie !")
            # si playerTurn est égal a namePlayer1
            if playerTurn == namePlayer1 : 
                # on ajoute +1 a notre variable scoreJ1
                scoreJ1 += 1   
            # sinon
            else : 
                # on ajoute +1 a notre variable scoreJ2              
                scoreJ2 += 1
            # ! affichage ésthétique ! 
            print(" ")
            # on sort de la boucle
            break

        # si la fonction boardFilled() renvoie True
        if boardFilled(boardGame):  
            # on affiche "Egalité !"
            print("Egalité !")     
            # ! affichage ésthétique ! 
            print(" ")       
            # on sort de la boucle 
            break     
        
        # si playerTurn est égal a playerFirst
        if playerTurn == playerFirst :        
            # alors
            # on passe la valeur de playerTurn a PlayerSecond  
            playerTurn = playerSecond           
            # on passe la valeur de coupPlayerTurn a coupPlayerSecond  
            coupPlayerTurn = coupPlayerSecond
        # sinon
        else :
            # on passe la valeur de playerTurn a playerFirst  
            playerTurn = playerFirst
            # on passe la valeur de coupPlayerTurn a coupPlayerFirst  
            coupPlayerTurn = coupPlayerFirst

    # on affiche "Rejouez ? ( y ) yes ou ( n ) no "
    print("Rejouez ? ( y ) yes ou ( n ) no ")
    # on donne la valeur de l'input du joueur a la variable replay
    replay = input(" > ")

    # si replay est égal a "y"
    if replay == "y":
        # alors 
        # on affiche "Score de (nom j1) : (scorej1) "
        print("Score de " + str(namePlayer1) + " : " + str(scoreJ1))
        # alors on affiche "Score de (nom j2) : (scorej2) "
        print("Score de " + str(namePlayer2) + " : " + str(scoreJ2))
        # ! affichage ésthétique ! 
        print(" ")
        # on rappel notre fonction ticTacToeStart() de maniere recursive avec comme arguments namePlayer1 le nom du J1, scoreJ1 et scoreJ2
        ticTactToeStart(namePlayer1, scoreJ1, scoreJ2 )

    # sinon
    else:
        # ! affichage ésthétique ! 
        print(" ")
        # on affiche "Score final de (nom j1) : (scorej1) "
        print("Score final de " + str(namePlayer1) + " : " + str(scoreJ1))
        # on affiche "Score final de (nom j1) : (scorej1) "
        print("Score final de " + str(namePlayer2) + " : " + str(scoreJ2))
        # ! affichage ésthétique ! 
        print(" ")
        # on affiche "Fin du Jeu"
        print("Fin du jeu !")
        # ! affichage ésthétique ! 
        print(" ")

# on appelle notre fonction ticTactToeStart() avec comme argument notre nom de joueur / cet appel sert a lancer le jeu
ticTactToeStart("Joueur")