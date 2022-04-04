
def push(stack, element):
    global top,stack_list
    if(top == size):
        print("\n******** Stack is Overflow ******** \n")

    else:
        top = top + 1
        stack_list += " "
        stack_list[top] = element
        print(f"\n{element} Added Successfully in stack")
        

def pop(stack):
    global top,stack_list
    # print(stack_list)
    if(top==-1):
        print("\n******** Stack is underflow ********\n   Please First Enter a element \n")

    else:
        val = stack_list[top]
        stack_list = stack_list[:top]
        top = top - 1
        print(f"\nremoved value from stack is {val}")
        

def peep(stack):
    global top,stack_list
    if(top==-1):
        print("\n******** Stack is Empty ******** \n")   

    else:
        top_value = stack_list[top]
        print(f"\nTop element of Stack : {top_value} ") 
        
print("\n {:*^60s} \n".format(" Welcome to Stack Program ")) 

checkSize = True 
while True:
    if(checkSize): 
        stackSize = int(input("\nEnter size of stack : "))
        if(stackSize > 0 ):
            checkSize = False 
            size = stackSize -1
            stack_list = []
            top = -1

        else:
            checkSize = True
            print("\nPlease enter size positive and greater than zero \n")
  

        
    if(checkSize == False):
            choice   = int(input("\nEnter you choice Number:\n[1] Push \n[2] pop \n[3] peep  \n[4] Exit \n" ))

            if(choice == 1):
                push(stack_list , input("\nEnter a element : "))

            elif(choice == 2):
                pop(stack_list)
            elif(choice == 3):
                 peep(stack_list)   
            elif(choice == 4):
               
                print("Thank you for doing some operations \n")
                break   
            else:
                print("******* Invalid  Number *********")    

