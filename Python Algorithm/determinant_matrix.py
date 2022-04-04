print("\n{:*^60s}".format(" Welcome to Diterminnet Matrix Program "))


def subMatrix(mainMatrix, row, j):
    newMatrix = [ [j for j in i] for i in mainMatrix]
    newMatrix = newMatrix[row+1:]
    list_d = []
    k = 0
    for list_c in newMatrix:
        list_d += " "
        list_d[k] = list_c[:j] + list_c[j+1:]
        k += 1  
    return list_d   



def determinant_matrix(lst):
    number_rows = 0 
    for i in lst:
        number_rows += 1    
    if(number_rows  == 2):
        normal_matrix = lst[0][0] * lst[1][1] - lst[1][0]*lst[0][1]
        return normal_matrix
        
    else:
        main_ans = 0 
         
        number_column = number_rows
        for j in range(number_column):
            sub_ans = (-1) ** (0+j) * lst[0][j] * determinant_matrix(subMatrix(lst, 0, j ))

            main_ans += sub_ans
        
        return main_ans  


checkCondition = True
lst = [ True for i in range(2)]

while(checkCondition):
        if(lst[0] == True):
            row = int(input("\nEnter  Row size for maxtriA : "))
            if(row > 0):
              lst[0] = False
            else:
                print("\nPlease enter size positive and greater than zero Row of maxtrix \n")
        elif(lst[1] == True):
            col = int(input("\nEnter  Col size for maxtriA : "))
            if(col > 0):
              lst[1] = False
            else:
                print("\nPlease enter size positive and greater than zero Column of maxtrix \n")


        if(lst[0] == False and lst[1] == False):
            if(row == col ):
                print("\n********* Enter value of maxtrix  ********* \n")
                maxtrixA = [ [0 for j in range(col)] for i in range(row)]

                for i in range(row):
                    # column = []
                    column =  [i  for i in range(row)]
                    for j in range(col):
                         value = int(input(f"\nEnter value of [{i+1}][{j+1}] : "))
                         column[j] = value
                    maxtrixA[i] = column

                print("\n***** Matrix *****\n ")
                for i in maxtrixA:
                    for value in  i:
                       print(value , end=" ")
                    print("")
                checkCondition = False    
            else:
                print("\nPlease Enter same order row and column of matrix \n") 
                lst[0] = True
                lst[1] = True               




ans = determinant_matrix(maxtrixA,)
print("\nResult : ",  ans)