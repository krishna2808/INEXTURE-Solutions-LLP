'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

'''


print()
while(True):
    n = input("Enter number : ")
    if(n.isnumeric()):
        n = int(n)
        for i in range(n):
            for j in range(n):
                if(j<=i):
                   print(j+1,end=" ")
            print()
        break    

    else: 
        print("Invalid Input ")

     
