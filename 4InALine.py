
import msvcrt

quite = 1

while quite != 0 :

    width = int(input("please enter board width: "))
    height = int(input("please enter board height: "))

    move = 99


    board = []   # board wat print as ons skuif met pyl

    for x in range(height) :

        tempBoard = []
                                                    #                  print('')
        for y in range(width) :                                  #print(" X" , end = '' )

            tempBoard.append(" *")                                                                            #print(" *" , end = '' )

        board.append(tempBoard)                       #set board dimens run net 1 keer dink ek



    winner = "DRAW"
    gameOver = 1

    x = 0
    y = 0
    move = 99
    Enter = 1
    equal = 2
    

    while gameOver != 0:

        if equal%2 == 0:


            if move == 5 :

                equal += 1


                board[x][y] = " X"



                for a in range(height) :

                    print("")

                    for b in range(width) :

                        print((board[a][b]) , end= "")
                

                print(" ")


                ###########wintest


                for c in range(height) :

                    lineX = 0

                    for v in range(width) :

                        if board[c][v] == " *" :
                            lineX = 0

                        if board[c][v] == " O" :
                            lineX = 0

                        if board[c][v] == " X" :
                            lineX += 1

                        if lineX == 4 :
                            gameOver = 0
                            winner = " X"

                            print("******************************************************* ")
                            print("")
                            print( winner + "  IS THE WINNER")
                            print("")
                            print("press any button to continue / Press 0 to exit: ")
                            quite = int(msvcrt.getch())
                            print("")


                for v in range(width) :

                    lineX = 0

                    for c in range(height) :

                        if board[c][v] == " *" :
                            lineX = 0

                        if board[c][v] == " O" :
                            lineX = 0

                        if board[c][v] == " X" :
                            lineX += 1

                        if lineX == 4 :
                            gameOver = 0
                            winner = " X"


                            print("*******************************************************")
                            print("")
                            print( winner + "  IS THE WINNER")
                            print("")
                            print("press any button to continue / Press 0 to exit: ")
                            quite = int(msvcrt.getch())
                            print("")



                lineX = 0
                beginPuntX = 0
                beginPuntY = height -1
                        #

                while beginPuntX < width :

                    

                    lineX = 0
                    XX = beginPuntX
                    YY = beginPuntY

                    while XX < height and YY < width :

                        if board[XX][YY] == " *" :
                            lineX = 0

                        if board[XX][YY] == " O" :
                            lineX = 0

                        if board[XX][YY] == " X" :
                            lineX += 1

                        if lineX == 4 :
                            gameOver = 0
                            winner = " X"
                            print("*******************************************************")
                            print("")
                            print( winner + "  IS THE WINNER")
                            print("")
                            print("press any button to continue / Press 0 to exit: ")
                            quite = int(msvcrt.getch())
                            print("")

                        XX += 1
                        YY += 1


                    if beginPuntY == 0:
                        beginPuntX += 1
                    else :
                        beginPuntY -= 1



















                lineX = 0
                beginPuntX = 0
                beginPuntY = 0
                        #

                while beginPuntY < height :

                    

                    lineX = 0
                    XX = beginPuntX
                    YY = beginPuntY

                    while XX < height and YY < width :

                        if board[XX][YY] == " *" :
                            lineX = 0

                        if board[XX][YY] == " O" :
                            lineX = 0

                        if board[XX][YY] == " X" :
                            lineX += 1

                        if lineX == 4 :
                            gameOver = 0
                            winner = " X"
                            print("*******************************************************")
                            print("")
                            print( winner + "  IS THE WINNER")
                            print("")
                            print("press any button to continue / Press 0 to exit: ")
                            quite = int(msvcrt.getch())
                            print("")

                        XX -= 1
                        YY += 1


                    if beginPuntX == width:
                        beginPuntY += 1
                    else :
                        beginPuntX += 1



















                    
                    ###########wintest

                
                if winner == " X" :
                    move = 0
                else :
                    move = int(msvcrt.getch())                 
        
                

            else :

                if move == 99 :
                    board[x][y] = " x"
                else:
                    if board[x][y] == " x" :
                        board[x][y] = " *"

                if move == 6 :
                    y = y+1
                    if board[x][y] == " *" :
                        board[x][y] = " x"

                if move == 2 :
                    x = x+1
                    if board[x][y] == " *" :
                        board[x][y] = " x"

                if move == 8 :
                    x = x-1
                    if board[x][y] == " *" :
                        board[x][y] = " x"

                if move == 4 :
                    y = y-1
                    if board[x][y] == " *" :
                        board[x][y] = " x"



                for a in range(height) :

                    print("")

                    for b in range(width) :

                        print((board[a][b]) , end= "")
                
                print(" ")


                #for num in range(height) :
                    #if board[num]                                 ################### bra soek n ry met 4 X
                

                move = int(msvcrt.getch()) 
    
    
                                                    ### ons gebruik daai msvcrt en wag vir enter of n letter om aan te gaan en mainboard te save
        else: 
            
            
            if move == 5 :

                equal += 1
            
                board[x][y] = " O"



                for a in range(height) :

                    print("")

                    for b in range(width) :

                        print((board[a][b]) , end= "")
                
                print(" ")


                ###########wintest


                for c in range(height) :

                    lineO = 0

                    for v in range(width) :

                        if board[c][v] == " O" :
                            lineO += 1

                        if board[c][v] == " *" :
                            lineO = 0

                        if board[c][v] == " X" :
                            lineO = 0

                        if lineO == 4 :
                            gameOver = 0
                            winner = " O"

                            print("*******************************************************")
                            print("")
                            print( winner + "  IS THE WINNER")
                            print("")
                            print("press any button to continue / Press 0 to exit: ")
                            quite = int(msvcrt.getch())
                            print("")


                for v in range(width) :

                    lineO = 0

                    for c in range(height) :

                        if board[c][v] == " *" :
                            lineO = 0

                        if board[c][v] == " X" :
                            lineO = 0

                        if board[c][v] == " O" :
                            lineO += 1

                        if lineO == 4 :
                            gameOver = 0
                            winner = " O"


                            print("*******************************************************")
                            print("")
                            print( winner + "  IS THE WINNER")
                            print("")
                            print("press any button to continue / Press 0 to exit: ")
                            quite = int(msvcrt.getch())
                            print("")



            
                beginPuntX = 0
                beginPuntY = height -1
                        #

                while beginPuntX < width :
                    

                    lineO = 0
                    XX = beginPuntX
                    YY = beginPuntY

                    while XX < height and YY < width :

                        if board[XX][YY] == " *" :
                            lineO = 0

                        if board[XX][YY] == " X" :
                            lineO = 0

                        if board[XX][YY] == " O" :
                            lineO += 1

                        if lineO == 4 :
                            gameOver = 0
                            winner = " O"
                            print("*******************************************************")
                            print("")
                            print( winner + "  IS THE WINNER")
                            print("")
                            print("press any button to continue / Press 0 to exit: ")
                            quite = int(msvcrt.getch())
                            print("")

                        XX += 1
                        YY += 1


                    if beginPuntY == 0:
                        beginPuntX += 1
                    else :
                        beginPuntY -= 1












                lineO = 0
                beginPuntX = 0
                beginPuntY = 0
                        #

                while beginPuntY < height :

                    

                    lineO = 0
                    XX = beginPuntX
                    YY = beginPuntY

                    while XX < height and YY < width :

                        if board[XX][YY] == " *" :
                            lineO = 0

                        if board[XX][YY] == " X" :
                            lineO = 0

                        if board[XX][YY] == " O" :
                            lineO += 1

                        if lineO == 4 :
                            gameOver = 0
                            winner = " O"
                            print("*******************************************************")
                            print("")
                            print( winner + "  IS THE WINNER")
                            print("")
                            print("press any button to continue / Press 0 to exit: ")
                            quite = int(msvcrt.getch())
                            print("")

                        XX -= 1
                        YY += 1


                    if beginPuntX == width:
                        beginPuntY += 1
                    else :
                        beginPuntX += 1




















                    ###########wintest



                if winner == " O":
                    move = 0
                else :
                    move = int(msvcrt.getch())
        
                

            else :

                if move == 99 :
                    board[x][y] = " o"
                else:
                    if board[x][y] == " o" :
                        board[x][y] = " *"

                if move == 6 :
                    y = y+1
                    if board[x][y] == " *":
                        board[x][y] = " o"

                if move == 2 :
                    x = x+1
                    if board[x][y] == " *" :
                        board[x][y] = " o"

                if move == 8 :
                    x = x-1
                    if board[x][y] == " *" :
                        board[x][y] = " o"

                if move == 4 :
                    y = y-1
                    if board[x][y] == " *" :
                        board[x][y] = " o"










                for a in range(height) :

                    print("")

            
                    for b in range(width) :

                        print((board[a][b]) , end= "")



        

                print(" ")
                


                
                move = int(msvcrt.getch())
     


##############################################################################################


print("Have a nice day")