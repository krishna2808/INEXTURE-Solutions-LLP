
def enqueue(queue, element):
    global front,rear,queue_list, temp 
    if(rear == queueSize -1 or temp == queueSize ):
        print("\n******** Queue is Overflow ********\n")

    else:
        front = 0
        rear += 1 
        queue_list += " "
        queue_list[rear] = element
        temp += 1 
        print(f"\n{element} Added Successfully in queue")


def dequeue(queue):
    global front ,rear,queue_list, temp
    # print(queue_list)
    # print(queue)
    if(rear == -1 ):
        print("\n******** Queue is underflow ********\nPlease First Enter a element \n")   

    else:
        value = queue_list[front]
        print(f"\n{value} has been removed :\n")
        rear -= 1

        queue_list = queue_list[front+1:]
        if queue_list == []:
            front=rear=-1
        print(queue_list)

def peek(queue):
    global front,queue_list
    if(front == -1):
        print("******** Queue is Empty ******** \n")   

    else:
        front_value = queue_list[front]
        print(f"Front element of Queue  : {front_value} ") 


print("\n {:*^60s} \n".format(" Welcome to Queue Program ")) 
checkSize = True 



while True:
    if(checkSize): 
        queueSize = int(input("\nEnter size of Queue  : "))
        if(queueSize > 0 ):
            checkSize = False 
            queue_list = []
            front = -1
            rear = -1
            temp = 0 
        else:
            checkSize = True
            print("\nPlease enter size positive and greater than zero \n")
  

        
    if(checkSize == False):
  


        choice   = int(input("\nEnter you choice Number:\n[1] Enqueue \n[2] Dequeue \n[3] peek \n[4] Exit \n" ))

        if(choice == 1):
           enqueue(queue_list, input("\nEnter a element : "))

        elif(choice == 2):
            dequeue(queue_list)
        elif(choice == 3):
            peek(queue_list)   
        elif(choice == 4):
            
            print("\nThank you for doing some operations \n")
            break        
        else:
            print("\n******* Invalid  Number *********")     

