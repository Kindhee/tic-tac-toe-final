# DEBUT

# on importe la fonction randint de la librairie random 

# on déini une fonction showBoardGame() avec comme argument boardCreated qui est le plateau de jeu créer / elle sert a afficher le tableau de jeu
    # on créer une boucle for qui parcours toutes les lignes de notre plateau
            # on créer une boucle for qui parcours tout les éléments de notre plateau
                # on affiche chaque élément avec deux espace a la fin grace a end = "  "
            # on affiche avec un retour a la ligne après chaque ligne de 3 éléments 

# on déini une fonction changeElement() avec comme arguments board qui est notre plateau de jeu, row les lignes du plateau, col les colonnes du plateau et coup le coup ( soit "X" soit "O" )
        # on change la valeur de notre plateau avec un index de ligne et de colonne par le coup du joueur 

# on déini une fonction playerGoingFirst() sans argument / elle renvoie un nombre aléatoire entre 1 et 2 pour choisir un joueur aléatoirement
    # on retourne un nombre aléatoire entre 1 et 2 avec randint(1, 2)

# on déini une fonction playerWin() avec comme arguments board qui est notre plateau de jeu et player le coup du joueur ( soit "X" soit "O" ) / elle teste si un des deux joueur a gagné 
    # on donne la valeur de None a une varibale win
    # on donne la valeur de len(board) a une varibale n
    # on créer une boucle for qui parcours tout les index i des éléments de notre plateau
        # on donne la valeur de True a la varibale win
        # on créer une boucle for qui parcours tout les index j des éléments de notre plateau 
            # on créer une condition if qui teste si notre plateau a un index de ligne et de colonne donné est différent de player
                # alors 
                # on donne la valeur de False a la varibale win
                # on utilise un break pour sortir des boucles 
        # on créer une condition if qui teste si win est égale a True 
            # alors
            # on retourne win

    # on créer une boucle for qui parcours tout les index i des éléments de notre plateau
        # on donne la valeur de True a la varibale win
        # on créer une boucle for qui parcours tout les index j des éléments de notre plateau 
            # on créer une condition if qui teste si notre plateau a un index de ligne et de colonne donné est différent de player
                # alors 
                # on donne la valeur de False a la varibale win
                # on utilise un break pour sortir des boucles 
         # on créer une condition if qui teste si win est égale a True 
            # alors
            # on retourne win

    # on donne la valeur de True a la varibale win
    # on créer une boucle for qui parcours tout les index i des éléments de notre plateau
        # on créer une condition if qui teste si notre plateau a un index de ligne et de colonne donné est différent de player
                # alors 
                # on donne la valeur de False a la varibale win
                # on utilise un break pour sortir des boucles 
    # on créer une condition if qui teste si win est égale a True 
        # alors
        # on retourne win

    # on donne la valeur de True a la varibale win
    # on créer une boucle for qui parcours tout les index i des éléments de notre plateau
        # on créer une condition if qui teste si notre plateau a un index de i et n - 1 - i est différent de player
            # alors 
            # on donne la valeur de False a la varibale win
            # on utilise un break pour sortir des boucles 
    # on créer une condition if qui teste si win est égale a True 
        # alors
        # on retourne win
    # sinon on retourne False

# on déini une fonction boardFilled() avec comme argument board qui est notre plateau de jeu / elle teste si le plateau de jeu est remplis
    # on créer une boucle for qui parcours toutes les lignes de notre plateau
        # on créer une boucle for qui parcours tout les éléments de notre plateau
            # on créer une condition if qui teste si un éléments donné est égale a '-' 
                # alors
                # on retourne False
    # sinon on retourne True

# on déini une fonction ticTactToeStart() avec comme arguments namePlayer1, namePlayer2, scoreJ1 défini comme égale a 0 et scoreJ1 défini comme égale a 0 / elle contient notre jeu
    # on affiche "Vous avez démarré une partie de Tic Tac Toe !"
    # ! affichage purement esthétique !
    # on donne la valeur de False a une varibale winJ1
    # on donne la valeur de False a une varibale winJ2
    # on donne la valeur retournée par la fonction playerGoingFirst() a une varibale indexPlayer
    # on créer une condition if qui teste si indexPlayer est égale a 1

        # alors
        # on affiche "Le J1 : (nom du joueur 1) commence !"
        # on donne la chaine de caractères namePlayer1 a la variable playerFirst
        # on donne la chaine de caractères namePlayer2 a la variable playerSecond
    # on créer une condition elif qui teste sinon si indexPlayer est égale a 2 
        # on affiche # on affiche "Le J2 : (nom du joueur 2) commence !"
        # on donne la chaine de caractères namePlayer2 a la variable playerFirst
        # on donne la chaine de caractères namePlayer1 a la variable playerSecond
        
    # on donne la chaine de caractères 'X' a la variable coupPlayerFirst
    # on donne la chaine de caractères 'O' a la variable coupPlayerSecond
    # on affiche "Début de la partie !"
    # ! affichage purement esthétique !
    # on donne une liste de 3 listes avec chacune 3 éléments '-' a la variable boardGame
    # on appelle notre fonction showBoardGame() avec en argument notre plateau de jeu boardGame
    # ! affichage purement esthétique !
    # on donne comme valeur playerFirst a notre variable playerTurn
    # on donne comme valeur coupPlayerFirst a notre variable coupPlayerTurn
    # on défini une liste vide coupAlreadyMade
    # on créer une boucle while qui se répète tant que winJ1 ou winJ2 sont égale a False

        # on affiche "Tour de : (nom joueur jouant a ce tour)"
        # on donne la valeur de False a la variable coupAvailable
        # on donne la valeur de False a la variable validationTest
        # on créer une boucle while qui se répète tant que coupAvailable est égale a False      
            # on créer une boucle while qui se répète tant que validationTest est égale a False
                # on affiche "Entrez un numéro de ligne : "
                # on demande un input en int dans la variable row qui sera le numéro de ligne
                # on affiche "Entrez un numéro de colonne : "
                # on demande un input en int dans la variable col qui sera le numéro de colonne
                # on créer une condition if qui teste si [row,col] n'est pas déjâ dans la liste coupAlreadyMade
                    # alors
                    # on ajoute [row,col] dans notre liste coupAlreadyMade
                    # on change la valeur de coupAvailable a True

                # ! affichage purement esthétique !
                # on teste
                    # on appelle la fonction changeElement avec comme arguments boardGame notre plateau de jeu, row notre numéro de ligne, col notre numéro de colonne et coupPlayerTurn son coup soit 'X' soit 'O'
                    # on quitte la boucle
                # si l'erreur IndexError est renvoyé 
                    # on affiche "Coup non valide rentrez un nombre entre 0 et 2"
                    # ! affichage purement esthétique !
        # on appelle notre fonction showBoardGame() avec en argument notre plateau de jeu boardGame
        # ! affichage purement esthétique !

        # on créer une condition if qui teste si la fonction playerWin() avec comme argmuments boardGame notre plateau de jeu, coupPlayerTurn son coup soit 'X' soit 'O', renvoie True
            # alors
            # on affiche "(nom joueur jouant a ce tour) a gagné la partie !"
            # on créer une condition if qui teste si la variable playerTurn est égale a la variable namePlayer1
                # alors
                # on incrémente la variable scoreJ1 de + 1 
            # sinon 
                # on incrémente la variable scoreJ2 de + 1 
            # ! affichage purement esthétique !
            # on quitte la boucle
        
        # on créer une condition if qui teste si la fonction boardFilled() avec comme argument boardGame notre plateau de jeu renvoie True
            # on affiche "Egalité !"
            # ! affichage purement esthétique !
            # on quitte la boucle 
        
        # on créer une condition if qui teste si la variable playerTurn est égale a la variable playerFirst
            # alors
            # la variable playerTurn est égale a la valeur de la variable playerSecond
            # la variable coupPlayerTurn est égale a la valeur de la variable coupPlayerSecond
        # sinon
            # la variable playerTurn est égale a la valeur de la variable playerFirst
            # la variable coupPlayerTurn est égale a la valeur de la variable coupPlayerFirst
    
    # on affiche "Rejouez ? ( y ) yes ou ( n ) no "
    # on donne la valeur d'un input en str a une variable replay

    # on créer une condition if qui teste si la variable replay est égale a "y"
        # alors 
        # on affiche "Score de (nom du joueur 1) : (score du joueur 1)"
        # on affiche "Score de (nom du joueur 2) : (score du joueur 2)"
        # ! affichage purement esthétique !
        #on appelle notre fonction ticTactToeStart() de manière récursive avec comme arguments namePlayer1 le nome du joueur 1, namePlayer2 le nome du joueur 2, scoreJ1 le score du joueur 1 et scoreJ2 le score du joueur 2 
    # sinon
        # ! affichage purement esthétique !
        # on affiche "Score final de (nom du joueur 1) : (score du joueur 1)"
        # on affiche "Score final de (nom du joueur 2) : (score du joueur 2)"
        # ! affichage purement esthétique !
        # on affiche "Fin du jeu !"
        # ! affichage purement esthétique !

# on appel notre fonction ticTactToeStart() avec en arguments les noms des deux joueurs en str ("nom joueur 1", "nom joueur 2") on peut aussi préciser scoreJ1 et scoreJ2 en arguments pour commencer avec des points dans les scores de chacun

# FIN