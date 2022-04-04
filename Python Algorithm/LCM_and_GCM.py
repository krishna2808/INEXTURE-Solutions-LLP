def factorOfNumber(factor):
    # for num in range(1, factor+1):
    factorLst = [] 
    for num in range(1, int(factor**(1/2))+1):
       if(factor%num == 0):
           factorLst.append(num)
           if(factor//num != num):
              factorLst.append(factor//num)
    factorLst = sorted(factorLst)
    if(len(factorLst) == 2):
        return True
    return False


def gcf(firstValue, secondValue):
    if(firstValue == 0):
       return secondValue
    return gcf( secondValue % firstValue, firstValue)

def lcm(firstValue, secondValue):
    # return (firstValue * secondValue)//gcf(firstValue, secondValue)
    if(firstValue == 0 or  secondValue == 0):
    	return 0 
    isPrimeFirst, isPrimeSecond = factorOfNumber(firstValue), factorOfNumber(secondValue)
    if(isPrimeFirst and isPrimeSecond):
        # print("------------------", firstValue, secondValue)
        if(firstValue != secondValue):
           return  firstValue * secondValue
        return firstValue   
    elif(isPrimeFirst or isPrimeSecond):
        # if(isPrimeFirst):
            # if(isPrimeSecond):
        #         return  firstValue*secondValue
        # elif(isPrimeSecond):
            return  firstValue*secondValue    

    multi = 1 
    if(firstValue > secondValue):
       maxValue = firstValue 
    else:
       maxValue = secondValue

    for i in range(2, maxValue+1):
        if(firstValue ==1 and secondValue ==1 ):
            break 
        while(firstValue%i == 0 or secondValue % i == 0):
            multi *= i 
            if(firstValue % i == 0 ):
              firstValue = firstValue//i 
            if(secondValue % i == 0 ):
               secondValue = secondValue//i 
    return multi  

isContinue =  True 
while(isContinue):
    numberOfElement =  input("\nEnter number of Element : ")
    if(numberOfElement.isnumeric()):
        numberOfElement = int(numberOfElement)
        numberOfElementList = []

        for i in range(numberOfElement):
            element = input(f"Enter {i+1} value :  ")

            if(element.isnumeric()):
                    numberOfElementList.append(int(element))
            else:
                print('\nEnter valid input as Number \n')
                break 
        if(numberOfElement == len(numberOfElementList)):
            break         
    else:
        print('Enter valid input as Number ')        	
                            	

# numberOfElementList = [ int(input(f"Enter {i+1} value :  ")) for i in range(numberOfElement)]


if(numberOfElement == len(numberOfElementList)):

    if(numberOfElement > 1):
        firstValue = numberOfElementList[0]
        for i in range(1, numberOfElement):
            ansOfGcf = gcf(firstValue , numberOfElementList[i])
            firstValue = ansOfGcf 

        firstValue = numberOfElementList[0]    

        for i in range(1, numberOfElement):
            ansOfLcm = lcm(firstValue , numberOfElementList[i])
            firstValue = ansOfLcm
        print("GCF : ", ansOfGcf)
        # print("LCM :  %.f" % ansOfLcm)
        print("LCM : ", ansOfLcm)
    else:
        print("Input should be greater than 1 ")    
else:
    print("Invalid input \n")    