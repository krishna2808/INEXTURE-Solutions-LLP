import random

# ----------------------  scoregameBox --------------------------------------

def scoregameBox(player1_name, player2_name):
    global player1_score, player2_score

    print("\n{0:-^50s}".format(" Score gameBox "))
    print(f"{player1_name} Score : {player1_score}\n{player2_name} Score : {player2_score} ")
    print("{0:-^50s}".format(''))


# --------------------------- Who is win -----------------------------------

def isWin(player1_name, player2_name):
    global player1_score, player2_score

    # ----------------- Player 1 checking conditions  --------------
    # check horizontal 
    for i in range(0,9,3):
        if(gameBox[i] == 'X' and gameBox[i+1] == 'X' and gameBox[i+2] == 'X'):
            print(f"***** {player1_name}  Win ***** ")
            player1_score += 1 
            return 1 
     # check Vertical 
    for i in range(0, 3):
        if(gameBox[i] == 'X' and gameBox[i+3] == 'X' and gameBox[i+6] == 'X'):
          print(f"***** {player1_name}  Win ***** ")
          player1_score += 1    
          return 1 
    
    # check diagonal 
    if(gameBox[0] == 'X' and gameBox[4] == 'X' and gameBox[8] == 'X'):
      player1_score += 1
      print(f"***** {player1_name}  win ***** ")
      return 1 
    if(gameBox[2] == 'X' and gameBox[4] == 'X' and gameBox[6] == 'X'):
      player1_score += 1
      print(f"***** {player1_name}  Win ***** ")
      return 1

    # ----------------- Player 2 checking conditions  --------------
    # check horizontal 
    for i in range(0,9,3):
        if(gameBox[i] == 'O' and gameBox[i+1] == 'O' and gameBox[i+2] == 'O'):
          player2_score += 1
          print(f"***** {player2_name}  Win ***** ")
          return 1 
     # check Vertical 
    for i in range(0, 3):
        if(gameBox[i] == 'O' and gameBox[i+3] == 'O' and gameBox[i+6] == 'O'):
          player2_score += 1
          print(f"***** {player2_name}  Win ***** ")
          return 1 
    # check diagonal 

    if(gameBox[0] == 'O' and gameBox[4] == 'O' and gameBox[8] == 'O'):
      print(f"{player2_name}  Win !!")
      player2_score += 1
      return 1 
    if(gameBox[2] == 'O' and gameBox[4] == 'O' and gameBox[6] == 'O'):
      player2_score += 1    
      print(f"***** {player2_name}  Win ***** ")
      return 1
    return  0 

# -------------------- Show gameBox -------------------------------------

def showGameBox():
    k = 3 
    print("\n\t{0:=^40s} \n".format(' Show Place '))
    for i in range(len(gameBox)):
        if(i<k):
            print('\t  '+str(i+1)+ ' ' +'|', end=" ")
            if(i==k-1):
                k += 3 
                print('\n\t{0:-^22s}'.format(''))

    print("\n\t{0:=^40s}\n".format(''))

# ------------------- update game Box after user or computer input ------------------------    

def updateGameBox(player_name, char):
        k = 3 
        print("\n\t{0:=^40s} \n".format(' '+player_name+ ' "'+char+'" Entered '))
        for i in range(len(gameBox)):
            if(i<k):
                print('\t   '+gameBox[i]+ ' ' +'|', end=" ")
                if(i==k-1):
                    k += 3 
                    print('\n\t{0:-^22s}'.format(''))
        print("\n\t{0:=^40s}\n".format(''))

# ------------------- Show empty Game Box for starting game ---------------- 


def emptyPlace():
    k = 3 
    for i in range(len(gameBox)):
        if(i<k):
            print('\t   '+gameBox[i]+ ' ' +'|', end=" ")
            if(i==k-1):
                k += 3 
                print('\n\t{0:-^22s}'.format(''))
    print("\n\t{0:=^40s}\n".format(''))

# -----------------------  Play with friend -------------------------------------

def playWithFriend(player1_name, player2_name):
    showGameBox()
    emptyPlace()
   

    total_number_of_time = 0
    end_of_game = 0 
    player = 1 
    while(True):
        end_of_game = isWin(player1_name, player2_name)
        if(total_number_of_time == 9  or end_of_game == 1):
            if(total_number_of_time == 9 and end_of_game == 0):
                print(" **** Game is draw ! ****** ")
            break 
        while(True):
            if(player==1):
                player_1 = input(f'{player1_name} Enter Your Place  : ')
                if(player_1.isnumeric()):
                    player_1 = int(player_1)
                    if(player_1>0 and player_1<=9 and gameBox[player_1-1] == ' '):
                       gameBox[player_1-1] = 'X'
                       updateGameBox(player1_name, computer_or_player1_char)
                       player = 2 
                       break 
                    else:
                        print("\nInvalid Input Please try again .... ")
                        continue 
                else:
                    print("\nInvalid Input Please try again .... ")
                    continue         

            else:

                player_2 = input(f'{player2_name} Enter Your Place  : ')
                if(player_2.isnumeric()):
                    player_2 = int(player_2)
                    if(player_2>0 and player_2 <=9 and gameBox[player_2-1] == ' '):
                        gameBox[player_2-1] = 'O'
                        updateGameBox(player2_name, human_or_player2_char)
                        player = 1 
                        break
                    else:
                        print("\nInvalid Input Please try again .... ")
                        continue 
                else: 
                    print("\nInvalid Input Please try again .... ")
                    continue 
                            
        total_number_of_time += 1 

def checkDraw():
    for index in range(len(gameBox)):
        if (gameBox[index] == ' '):
            return False
    return True



def whoIsWon(char):
    if gameBox[0] == gameBox[1] and gameBox[0] == gameBox[2] and gameBox[0] == char:
        return True
    elif (gameBox[3] == gameBox[4] and gameBox[3] == gameBox[5] and gameBox[3] == char):
        return True
    elif (gameBox[6] == gameBox[7] and gameBox[6] == gameBox[8] and gameBox[6] == char):
        return True
    elif (gameBox[0] == gameBox[3] and gameBox[0] == gameBox[6] and gameBox[0] == char):
        return True
    elif (gameBox[1] == gameBox[4] and gameBox[1] == gameBox[7] and gameBox[1] == char):
        return True
    elif (gameBox[2] == gameBox[5] and gameBox[2] == gameBox[8] and gameBox[2] == char):
        return True
    elif (gameBox[0] == gameBox[4] and gameBox[0] == gameBox[8] and gameBox[0] == char):
        return True
    elif (gameBox[6] == gameBox[4] and gameBox[6] == gameBox[2] and gameBox[6] == char):
        return True
    else:
        return False




# --------------------   MinMax Algorithm -------------------------------------

def minimax(gameBox, depth, isMaximizing):
    if (whoIsWon(computer_or_player1_char)):
        return 1
    elif (whoIsWon(human_or_player2_char)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        bestScore = -50
        for index in range(len(gameBox)):
            if (gameBox[index] == ' '):
                gameBox[index] = computer_or_player1_char
                score = minimax(gameBox, depth + 1, False)
                gameBox[index] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 50
        for index in range(len(gameBox)):
            if (gameBox[index] == ' '):
                gameBox[index] = human_or_player2_char
                score = minimax(gameBox, depth + 1, True)
                gameBox[index] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore




                             
# ------------------- user play with  computer  hard level -----------





def playWithComputer(player1_name, player2_name):
    global getIndexPlayer
    getIndexPlayer = 0 
    showGameBox()
    emptyPlace()
    end_of_game = 0 
    isCont, isContinue = True, True
    firstComputerInput  = True
    total_number_of_time = 0
    choice  = input("Enter First Tearn :\n[1] Computer [2] Human  : ")
    if(choice.isnumeric()):
        choice = int(choice)

        if(choice ==1):
              player = 1 
        elif(choice == 2):
           player = 2
        else:
           print("\nPlease Enter valid choice \n")
           return    
    else:
        print("\nPlease Choice as Number \n")   
        return  
               


    while(isCont):
        if(total_number_of_time == 9):
            print(" **** Game is draw  Try Again !! ****** ")
            updateGameBox(player1_name, computer_or_player1_char)
            scoregameBox(player1_name, player2_name)

            break 
        while(isContinue):
                if(player==1):
                    bestScore = -50
                    bestMove = 0
                    for index in range(len(gameBox)):
                        if (gameBox[index] == ' '):
                            gameBox[index] = computer_or_player1_char
                            # print('inital ', gameBox)
                            score = minimax(gameBox, 0, False)
                            # print('computer Move score ', score)

                            gameBox[index] = ' '
                            # print('inital ', gameBox)

                            if (score > bestScore):
                                bestScore = score
                                # print('best score ', bestScore)
                                bestMove = index

                    # insertLetter(computer_or_player1_char, bestMove)
                    gameBox[bestMove] = computer_or_player1_char
                    print(f'{player1_name}  Choose Place  : {bestMove+1}')  
                    total_number_of_time += 1 
                    updateGameBox(player1_name, computer_or_player1_char)

                    if(isWin(player1_name, player2_name)):
                            scoregameBox(player1_name, player2_name)
                            isCont = False
                            isContinue = False

                            break 
                    else: 
                            if(total_number_of_time == 9):
                                isContinue = False
                                break 
                            player = 2 
                else:

                    player2_place = input(f'{player2_name} Enter Your Place  : ')
                    if(player2_place.isnumeric()):
                        player2_place = int(player2_place)
                        if(player2_place >0 and player2_place <=9 and gameBox[player2_place-1] == ' '):
                            gameBox[player2_place-1] = 'O'
                            getIndexPlayer =  player2_place - 1 
                            updateGameBox(player2_name, human_or_player2_char)
                            if(isWin(player1_name, player2_name)):
                                scoregameBox(player1_name, player2_name)
                                isCont = False
                                isContinueFriend = False
                                break
                            else:    
                                total_number_of_time += 1 

                                player = 1 
                                break
                        else:
                            print("\nInvalid Input Please try again .... \n")
                            continue 
                    else:
                        print("\nInvalid Input Please try again .... \n")
                        continue 
                                
                       
# --------------------------------- play with computer normal level -------------------

def normalComputer(player1_name, player2_name):
    showGameBox()
    emptyPlace()
    total_number_of_time = 0
    end_of_game = 0 
    
    
    choice =  input("\nChoice First Tearn :\n[1] Computer [2] Human  : ")
    if(choice.isnumeric()):
        choice = int(choice)    
        if(choice ==1):
            player = 1

            updateGameBox(player1_name, computer_or_player1_char)
        elif(choice == 2):
           player = 2
        else:
           print("\nPlease Enter valid choice \n")
           return    
    else:
        print("\nPlease Choice as Number \n")   
        return        

    
    while(True):
        end_of_game = isWin(player1_name, player2_name)
        if(total_number_of_time == 9  or end_of_game == 1):
            if(total_number_of_time == 9 and end_of_game == 0):
                    print(" **** Game is draw  Try Again !! ****** ")
                    updateGameBox(player1_name, computer_or_player1_char)
                    scoregameBox(player1_name, player2_name)
            else: 
                 scoregameBox(player1_name, player2_name)

            break 
        while(True):
            if(player==1):
                player_1 = random.randint(1,10)
                if(player>0 and player_1<=9 and gameBox[player_1-1] == ' '):
                   print(f'{player1_name}  Choose Place  : {player_1}')
                   gameBox[player_1-1] = 'X'
                   updateGameBox(player1_name, computer_or_player1_char)
                   player = 2 
                   break 


                else:
                     continue 
            else:

                player_2 = input(f'{player2_name} Enter Your Place  : ')
                if(player_2.isnumeric()):
                    player_2 = int(player_2)
                    if(player_2>0 and player_2 <=9 and gameBox[player_2-1] == ' '):
                        gameBox[player_2-1] = 'O'
                        updateGameBox(player2_name, human_or_player2_char)
                        player = 1 
                        break
                    else:
                        print("\nInvalid Input Please try again .... \n")
                        continue 
                else: 
                    print("\nInvalid Input Please try again .... \n")
                    continue 
                            
        total_number_of_time += 1 



# --------------------- create empty Game Box ------------------------------

gameBox = [ ' ' for i in range(9)]
computer_or_player1_char = 'X'
human_or_player2_char = 'O'
getIndexPlayer = 0 
isContinueGame = True
while(isContinueGame):
   player1_score, player2_score  = 0, 0 
   print("\n[1] Play With Friend  \t[2] Play Normal Level With Computer \t[3] play Hard Level with computer \t[4] Quit\n")
   user_choice = input("Enter Your Choice : ")
   if(user_choice.isnumeric()): 
       user_choice = int(user_choice)
       
        # ------------------------ Play with Friend --------------------------------- 

       if(user_choice == 1):
            isContinueFriend, initial ,  = True, True
            while(isContinueFriend): 
               if(initial): 
                   player1 = input("Enter Player 1 Name : ")
                   player2 = input("Enter Player 2 Name : ")
                   initial = False
               gameBox = [ ' ' for i in range(9)]
               scoregameBox(player1, player2)
               playWithFriend(player1, player2)
               scoregameBox(player1, player2)
               n= input("[1] Continue....\t[2] Exit\nYour Choice : ")
               if(n.isnumeric()):
                   n = int(n)
                   if(n == 1):
                      isContinueFriend = True
                   elif(n == 2):
                       isContinueFriend = False
                   else:
                       print("\nWrong Input ")
                       break
               else:
                  print("\nWrong Input ")
                  break 
                          

        # -----------------   Play with normal level computer --------------------------------------

       elif(user_choice == 2):

            isContinueFriend, initial = True, True
            while(isContinueFriend): 
               if(initial):
                 player1 = 'Computer' 
                 player2 = input('Enter Your Name : ')
                 initial = False
               gameBox = [ ' ' for i in range(9)]
               scoregameBox(player1, player2)
               normalComputer(player1, player2)
               # scoregameBox(player1, player2)
               n = input("[1] Continue....\t[2] Exit\nYour Choice : ")
               if(n.isnumeric()):
                   n = int(n)
                   if(n == 1):
                      isContinueFriend = True
                   elif(n == 2):
                       isContinueFriend = False
                   else:
                       print("\nWrong Input ")
                       break 
               else:
                    print("\nWrong Input ")
                    break 

                                      
        # -----------------   Play with hard level computer --------------------------------------

       elif(user_choice == 3):
            isContinueFriend, initial = True, True
            while(isContinueFriend): 
               if(initial):
                 player1 = 'Computer' 
                 player2 = input('Enter Your Name : ')
                 initial = False
               gameBox = [ ' ' for i in range(9)]
               scoregameBox(player1, player2)
               playWithComputer(player1, player2)
               # scoregameBox(player1, player2)
               n= input("[1] Continue....\t[2] Exit\nYour Choice : ")
               if(n.isnumeric()):
                   n = int(n)
                   if(n == 1):
                      isContinueFriend = True
                   elif(n == 2):
                       isContinueFriend = False
                   else:
                       print("\nWrong Input ")
                       break     
               else:
                  print("\nWrong Input ")
                  break  
                                  
       elif(user_choice == 4):
            isContinueGame= False     
            print("Thank you !! ")
       else:
          print("\nInvalid Input \n")
   else: 
       print("\nInvalid Input \n")
      
