'''




        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

'''


print()
while(True):
   n = input("Enter number : ")
   print()
   if(n.isnumeric()):
      # n  = int(n)-1
      n  = int(n)
      if(n%2 != 0 and n > 2):
          initial = n//2 + 2
          last =  n//2

          for i in range(1, initial):
              for space in range((initial-1)-i):
                 print(" ", end=" ")
              for k in range(i*2 -1  ,0,-1):
                 print("*", end=" ")
              print() 
          n = n -2
          # print()
          for i in range(last,0,-1):
                for space in range(last, i-1 ,-1): 
                    print(" ", end=" ")
                for k in range(i*2 -1  ,0,-1):
                   print("*", end=" ")
                print() 
          break          
      else:
         print("only odd value consider or value is grether than three ")             
              
   else:
       print("Invalid input ")       
