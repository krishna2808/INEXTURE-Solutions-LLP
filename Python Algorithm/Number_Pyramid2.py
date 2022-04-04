'''

1
2 3
4 5 6
7 8 9 10

'''

print()
while(True):
    n = input("Enter number : ")
    if(n.isnumeric()):
       n  = int(n)
       value = 1 
       for i in range(n):
            for j in range(n):
                if(j<=i):
                    print(value, end=" ")
                    value += 1 
            print()
       break
    else:
         print("Invalid input")        

