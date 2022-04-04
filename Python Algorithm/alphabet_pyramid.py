'''
A
B B
C C C
D D D D
E E E E E

'''
print()
lst = [  chr(65+i) for i in range(26)]
while(True):
    # print(lst)
    n = input("Enter number : ")
    if(n.isnumeric()):
        n = int(n)
        for i in range(n):
            for j in range(n):
                if(j<=i):
                   print(lst[i%26],end=" ")
            print()
        break         

    else: 
        print("Invalid Input ")			
