'''
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *


'''



print()
while(True):
    n = input("Enter number : ")
    if(n.isnumeric()):
        n  = int(n)
        print()
        for i in range(n,0,-1):
            for space in range(n, i ,-1): 
                print(" ", end=" ")
            for k in range(i*2 -1  ,0,-1):
               print("*", end=" ")
            print() 
        break    
    else:
        print("Invalid Input ")         