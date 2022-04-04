'''

1 2 3 4 5
1 2 3 4 
1 2 3
1 2
1

'''


print()
while(True):
    n = input("Enter number : ")
    if(n.isnumeric()):
        n  = int(n)
        print()
        for i in range(n):
            k = 0
            for j in range(n):
                if(j>=i):
                    print(k+1 ,end=" ")
                    k += 1
            print()
        break    
    else:
        print("Invalid Input ")    
            