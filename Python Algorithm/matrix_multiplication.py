def matrix_multiplication():

    checkCondition = True
    lst = [ True for i in range(4)]
    while(checkCondition):
        if(lst[0] == True):
            rowA = int(input("Enter  Row size for maxtriA : "))
            if(rowA > 0):
              lst[0] = False
            else:
                print("\nPlease enter size positive and greater than zero Row of maxtriA \n")
        elif(lst[1] == True):
            colA = int(input("Enter  Col size for maxtriA : "))
            if(colA > 0):
              lst[1] = False
            else:
                print("\nPlease enter size positive and greater than zero Column of maxtriA \n")
        elif(lst[2] == True):
            rowB = int(input("Enter  Row size for maxtriB : "))

            if(rowB > 0):
              lst[2] = False
            else:
                print("\nPlease enter size positive and greater than zero Row  of maxtriB \n")

        elif(lst[3] == True):
            colB = int(input("Enter  Col size for maxtriB : "))


            if(colB > 0):
              lst[3] = False
              
            else:
                print("\nPlease enter size positive and greater than zero Column of maxtriB \n")
                        
        
        if(lst[0] == False and lst[1] == False and lst[2] == False and lst[3] == False):

            if(colA == rowB):
 
                # multiplication = [[0]*3]*3
                multiplication = [ [0 for j in range(colB)] for i in range(rowA)]
               

                
                print("\n********* Enter value of maxtrix A ********* \n")
                maxtrixA = [ [0 for j in range(colA)] for i in range(rowA)]
                # print(maxtrixA)

                for i in range(rowA):
                    column =  [0  for i in range(colA)]
                    # print(column)
                    for j in range(colA):
                        
                         value = int(input(f"\nEnter value of [{i+1}][{j+1}] : "))
                         column[j] = value
                    maxtrixA[i] = column

                print("\n***** Matrix A *****\n ")
                for i in maxtrixA:
                    for value in  i:
                       print(value , end=" ")
                    print("")



                print("\n********* Enter value of maxtrix B ********* \n")
                maxtrixB = [ [0 for j in range(colB)] for i in range(rowB)]

                for i in range(rowB):
                    column =  [0  for i in range(colB)]

                    for j in range(colB):
                        value = int(input(f"\nEnter value of [{i+1}][{j+1}] : "))
                        column[j] = value
                    maxtrixB[i] = column


                print("\n***** Matrix B ***** \n")
                for i in maxtrixB:
                    for value in  i:
                        print(value , end=" ")
                    print("")           


                for i in range(rowA):
                    for j in range(colB):
                        for z  in range(rowB):

                          multiplication[i][j] += maxtrixA[i][z] * maxtrixB[z][j] 

                print("\n********** Matrix of multiplication ************* \n")
                for i in multiplication:
                    for value in  i:
                        print(value , end=" ")       
                    print("")   
                checkCondition = False     
            else:
                 print("\nPlease Enter MatrixA of column and maxtrixB of Raw should be same \n") 
                 lst = [ True for i in range(4)] 

  
			
matrix_multiplication()