import random
countGuess = 0 

def compare_digit(randomNumber,number):
    cow,bull = 0,0
    rendomLst = [ char for char in randomNumber] 
    numLst = [ char for char in number]       
    for i in range(4):
        
        if(randomNumber[i] == number[i] ):
            cow = cow + 1
            rendomLst.remove(number[i])
            numLst.remove(number[i])
    for i in rendomLst:
        if(i in numLst):
           bull += 1 
           numLst.remove(i)

    return cow, bull

# randomNumber = 1123
# randomNumber = 2211

randomNumber   = random.randint(1000,9999)
print(randomNumber)
while True:

    guessNumber = input("\nEnter Four digit Number : ")
    if(guessNumber.isdigit()):
        if(len(guessNumber) == 4):
            cow,bull = compare_digit(str(randomNumber),guessNumber)
            countGuess += 1
            print(f"cows : {cow} and bulls : {bull} ")
            if(cow < 4):
                print("\nPlease Try again ... ")
            else:
                print(f"\nCongratulations you have won game and You have {countGuess} time guessed \n****** The number was {randomNumber} ****** ")
                break
        else:
            print("\n{0:*^60s}".format(' Please Enter four digit value.'))
    else:
        print("\n{0:*^60s}".format(' Please Enter four digit value.'))
