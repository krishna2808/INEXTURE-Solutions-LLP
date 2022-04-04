'''
        1
      2 3 2
    3 4 5 4 3
  4 5 6 7 6 5 4
5 6 7 8 9 8 7 6 5



'''


print()
while(True):
   n = input("Enter number : ")
   if(n.isnumeric()):
      n  = int(n)+1
      for i in range(1, n):
          for space in range((n-1)-i):
             print(" ", end=" ")
          mid = (i*2 -1)//2 
          initial =  0
          t = i-1 
          for k in range(i*2 -1  ,0,-1):
            if(initial <= mid):
                t += 1     
                print(t, end= " ")
                # print("*", end=" ")
            else:
                t -= 1 
                print(t, end= " ")
            initial += 1 
           
          print()  
      break      
   else:
       print("Invalid input ")       
