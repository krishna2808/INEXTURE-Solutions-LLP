def factorOfNumber(factor):
    # for num in range(1, factor+1):
    if(factor==0):
        print(0)
        return  
    factorLst = [] 
    for num in range(1, int(factor**(1/2))+1):
       if(factor%num == 0):
           factorLst.append(num)
           if(factor//num != num):
              factorLst.append(factor//num)
    print(sorted(factorLst))

factor = input("Enter number of Factor : ")
if(factor.isnumeric()):
    factor = int(factor)
    factorOfNumber(factor)
else:
    print("Invalid input")