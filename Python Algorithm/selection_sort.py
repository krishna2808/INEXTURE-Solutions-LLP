def selection_sort(lst,size):
    i = 0 
    # for i in range(size):
    while(i<size):
        min_Value_Index = i 
        j = min_Value_Index + 1 
        while(j<size):

        # for j in range(min_Value_Index + 1, size):
            if(lst[min_Value_Index] > lst[j]):
                min_Value_Index = j 
            j += 1     
        swap = lst[i]        
        lst[i] = lst[min_Value_Index]
        lst[min_Value_Index] = swap

        i += 1   
    return lst  
          
print("\n {:*^60s} ".format(" Welcome to Selection Program "))

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

        print(selection_sort(lst, size))  

    else:  
        checkCondition = True    
        print("\nPlease enter size positive and greater than zero \n")
