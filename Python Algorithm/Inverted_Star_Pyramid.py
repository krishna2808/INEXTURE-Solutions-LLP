'''

* * * * *
* * * *
* * * 
* *
*

'''


print()
while(True):
    n = input("Enter number : ")
    if(n.isnumeric()):
        n  = int(n)
        print()
        for i in range(n):
            for j in range(n):
                if(j>=i):
                    print("*" ,end=" ")
            print()
        break    
    else:
         print("Invalid Input ")        
                
