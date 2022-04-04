print("{:*^60s}".format("Welcome to pelindrome Program "))

def pelidrom_number(number):
    result, n  = 0, number 
    while(n>0):
        remainder = n%10
        result = result*10 + remainder
        n = n//10



    return  print("The number is a pelindrome ") if(result == number)  else print("The number isn't a pelindrome ")

pelidrom_number(int(input("Enter Your Number ")))      	
 
