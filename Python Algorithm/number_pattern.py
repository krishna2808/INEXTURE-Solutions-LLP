'''
           1
         1   1
       1   2   1
     1   3   3    1
   1  4    6   4   1
 1  5   10   10  5   1

'''


while(True):
    n = input("Enter number : ")
    if(n.isnumeric()):
        n  = int(n)+1  
        for i in range(n):
            for space in range(n-i-1):
                print(" ", end = "") 
            temp = 1     
            for j in range(1, i+1):
                  print(temp,  end= " ")
                  a = temp * (i-j)//j
                  temp = a 
            print()      
        break                  
    else:
        print("Invalid Input")    