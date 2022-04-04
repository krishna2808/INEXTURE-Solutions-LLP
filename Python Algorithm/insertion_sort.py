def insertion_sort(lst, size):
    i = 1
    while(i < size):
        value = lst[i]
        j = i -1
        while(value<=lst[j] and j>=0):
        	lst[j+1] = lst[j]
        	j -= 1 
        lst[j+1] =  value
        i += 1 
    return lst    



checkCondition = True
while checkCondition:
   

    size = int(input("Enter Your size of Array : "))

    if(size > 0 ):
        checkCondition = False
        lst = [] 
        i = 0 
        while i < size:
            lst += ' '
            lst[i] = int(input(f"Enter Your {i+1} Element : "))
            i += 1 

        print(insertion_sort(lst, size))     

    else:  
        checkCondition = True    
        print("\nPlease enter size positive and greater than zero \n")
