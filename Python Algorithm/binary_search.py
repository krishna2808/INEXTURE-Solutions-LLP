
def bubbleSort(lst, size):

    i = 0 
    while(i < size):
        j = 0 
        while(j < size-1-i):
            if(lst[j]>lst[j+1]):
                swap = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = swap
            j += 1 
        i += 1      

    return lst  
    



def binarySearch(lst, size, left, right, find): 
    if(left<= right):


        midIndex = (left+right)//2

    	
        if(lst[midIndex] == find):
            print('krishna 1 ')
            return f"----- {find} is  present in the List. -----\n"
    	
        elif(lst[midIndex]>find):
            print('krishna 2')
            return binarySearch(lst,size, left, midIndex-1, find)
    	
        else:
            print('krishna 3 ')
            return binarySearch(lst, size, midIndex+1, right, find)
    
    return f"---- {find} is NOT present in the List. -----\n"

print(" {:*^60s} ".format(" Welcome to Binary Search Program "))
checkCondition = True
while checkCondition:
   

    size = int(input("Enter Your size of Array : "))
    if(size > 0 ):
        checkCondition = False
        # lst = arr = [ int(input(f"Enter Your {i+1} Element : ")) for i in range(size)]
        lst = [] 
        i = 0 
        while i < size:
            lst += ' '
            lst[i] = int(input(f"Enter Your {i+1} Element : "))
            i += 1 

        lst = bubbleSort(lst, size)
        print(binarySearch(lst,size, 0, size-1, int(input("Enter value you want to find : "))))    

    else:  
        checkCondition = True    
        print("\nPlease enter size positive and greater than zero \n")

