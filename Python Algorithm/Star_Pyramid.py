'''

*
* *
* * *
* * * *
* * * * *
'''

print()

while(True):
    n = input("Enter number : ")
    if(n.isnumeric()):
        n  = int(n)
        for i in range(n):
            for j in range(n):
                if(j<=i):
                   print("*" ,end=" ")
                else:
                    break	
    			 # print("*",end=" ") if(j<=i) else break
            print()
        break     
    else:
        print("Invalid Input")		
			
