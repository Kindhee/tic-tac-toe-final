from random import randint

def showBoardGame(boardCreated):
        for row in boardCreated:          
            for item in row:  
                print(item, end="  ")
            print()

def changeElement(board, row, col, coup):
        board[row][col] = coup

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

def canWinTest(a, b, c, player):
    if a == b == player and c == '-':
        return[True, 2]
    elif c == a == player and b == '-':
        return[True, 1]
    elif b == c == player and a == '-':
        return[True, 0]
    else:
        return[False]
      
def canWin(board, player):
    for i in range(3):
        ligne = canWinTest(board[i][0], board[i][1], board[i][2], player)
        if ligne[0] == True:
            return i, ligne[1]
        colone = canWinTest(board[0][i], board[1][i], board[2][i], player)
        if colone[0] == True:
            return colone[1], i
    diagoUn = canWinTest(board[0][0], board[1][1], board[2][2], player)
    diagoDeux = canWinTest(board[0][2], board[1][1], board[2][0], player)
    if diagoUn[0] == True:
        return diagoUn[1], diagoUn[1]
    if diagoDeux[0] == True:
        return diagoDeux[1], 2-diagoDeux[1]
    return []

def iaPlay(board, iacoup, player, turn, coupAlreadyMade):
    # premier tour
    if turn == 1:
        # si on commence 
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
    # troisieme tour
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



def ticTactToeStart(namePlayer1, scoreJ1 = 0, scoreJ2 = 0):
    global coupAlreadyMade
    print("Vous avez démarré une partie de Tic Tac Toe !")
    print(" ")
    winJ1 = False
    winJ2 = False
    playerFirst = namePlayer1
    namePlayer2 = "IA"
    playerSecond = namePlayer2
    coupPlayerFirst = 'X'
    coupPlayerSecond = 'O'
    print("Début de la partie !")
    turn = 1
    print(" ")
    boardGame = [['-','-','-'],['-','-','-'],['-','-','-']]
    showBoardGame(boardGame)
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
                print(" ")
                try :
                    changeElement(boardGame,row,col,coupPlayerTurn)
                    break
                except IndexError :
                    print("Coup non valide rentrez un nombre entre 0 et 2")
                    print(" ")
            showBoardGame(boardGame)
            print(" ")

        elif playerSecond == namePlayer2:
            iaPlay(boardGame, coupPlayerSecond, coupPlayerFirst, turn, coupAlreadyMade) 
            turn += 1  
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
        ticTactToeStart(namePlayer1, scoreJ1, scoreJ2 )

    else:
        print(" ")
        print("Score final de " + str(namePlayer1) + " : " + str(scoreJ1))
        print("Score final de " + str(namePlayer2) + " : " + str(scoreJ2))
        print(" ")
        print("Fin du jeu !")
        print(" ")

ticTactToeStart("Gabriel")