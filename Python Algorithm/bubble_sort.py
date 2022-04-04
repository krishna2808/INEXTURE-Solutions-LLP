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


print(" {:*^60s} ".format(" Welcome to bubble Sort Program "))

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

        print(bubbleSort(lst, size))

    else:  
        checkCondition = True    
        print("\nPlease enter size positive and greater than zero \n")
