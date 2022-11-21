## premier tour
# if turn == 1:
    ## si on commence 
    # if playerFirst == joueur :
        ## si on joue milieu 
        # if playerCoup == [1,1]
            ## alors l'ia joue coin 
            # iaCoup = ( [0,0] dans un coin)
        ## si on joue coin 
        # if playerCoup == [0,0] / [2,0] / [0,2] / [2,2]
            ## alors l'ia joue milieu
            # iaCoup = [1,1]
        ## si on joue milieu de ligne sur les bords
        # if playerCoup == [0,1] / [1,0] / [2,1] / [1,2] 
            ## l'ia joue dans l'un des coins collés au coup du joueur
            # if playerCoup == [0,1] / [2,1] :
                # iaCoup = playerCoup [x,y+1]
            # if playerCoup == [1,0] / [1,2] :
                # iaCoup = playerCoup [x-1,y]
    ## sinon l'ia commence
    # if playerFirst == ia :
        ## l'ia joue milieu
        # iaCoup = [1,1]
## deuxième tour
# if turn == 2:
    ## si on a commence
    # if playerFirst == joueur :
        ## si on a joue  milieu
        # if [0,0] == playerCoup:
            ## si on joue toute les cases qui peuvent nous faire gagner 
            # if joueur canWin == True a [x,x]
                ## l'ia bloque la dernière case 
                # ia joue [x,y]
            ## si on joue la case qui s'aligne avec le coup de l'ia 
            # if joueur canWin != True
                ## l'ia joue le coin case opposé pour créer une ligne avec un coup au milieu manquant
                # if iaCoup == [0,0] / [2,0] :
                    # iaCoup = [x,y+2]
                # if iaCoup == [0,2] / [2,2] :
                    # iaCoup = playerCoup [x,y-2]
        ## si on a joue coin 
        # if [0,0] / [2,0] / [0,2] / [2,2]  == playerCoup:
            ## si on joue une case qui aligne deux de nos coups
            # if joueur canWin == True a [x,y]
                ## l'ia le bloque
                # ia joue [x,y]
            ## si on joue un coup qui n'aligne pas deux de nos coups
            # if joueur canWin != True
                ## l'ia aligne son deuxieme coup avec son premier et un espace vide
                # if [0,0] and [2,2] == playerCoup OR [0,2] and [2,0] == playerCoup:
                    # iaCoup = [1,0]
                # sinon:
                    ## place coin opposé au joueur
                    # if [2,2] == playerCoup:
                        # iaCoup = [0,0]
                    # if [2,0] == playerCoup:
                        # # iaCoup = [0,2]
                    # if [0,0] == playerCoup:
                        # # iaCoup = [2,2]
                    # if [0,2] == playerCoup:
                        # # iaCoup = [2,0]
        ## si on a joue milieu de ligne sur les bords
        # if [0,1] / [1,0] / [2,1] / [1,2]  == playerCoup: 
            ## si on joue une case qui aligne deux de nos coups
            # if joueur canWin == True a [x,x]
                ## l'ia bloque la dernière case 
                # ia joue [x,y]
            ## si on joue un coup qui n'aligne pas deux de nos coups
            # if joueur canWin != True
                ## l'ia aligne son deuxieme coup avec son premier et un espace vide 
## troisieme tour
# if turn == 3:
    ## si possibilité de gagner == True 
    # if ia canWin == True a [x,y]:
        ## gagner 
        # ia joue [x,y]
    ## si joueur possibilité de gagner == True
    # if joueur canWin == True a [x,y] :
        ## bloquer 
        # ia joue [x,y]
    ## sinon 
    # if joueur canWin != True :
        ## jouer pour aligner / remplir
        # ia joue [...,...]