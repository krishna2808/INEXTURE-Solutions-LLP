'''

        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *"


'''


print()
while(True):
   n = input("Enter number : ")
   if(n.isnumeric()):
      n  = int(n)+1
      for i in range(1, n):
          for space in range((n-1)-i):
             print(" ", end=" ")
          for k in range(i*2 -1  ,0,-1):
             print("*", end=" ")
          print()  
      break      
   else:
       print("Invalid input ")       
