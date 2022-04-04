def enqueue(arr, element):
    global front, rear, size
    if((rear+1) % size  == front):
        print("******** Queue is Overflow ********\n")
    elif(front == -1):
            front += 1
            rear += 1 
            arr[rear] = element 
            print(f"\n{element} Added Successfully in queue\n")
    else:
        rear = (rear + 1) % size  
        arr[rear] = element
        print(f"\n{element} Added Successfully in queue\n")

def dequeue(arr):
    global front, rear, size
    if(front == -1):
        print("******** Queue is underflow ********\n Please First Enter a element \n")
    elif(front == rear):
        removeElement = arr[front] 
        arr[front] = ""
        front = -1
        rear = -1 
        print(f"{removeElement} has been removed :\n")
    else:
        removeElement = arr[front]
        arr[front] = ""
        front = (front +1)% size
        print(f"{removeElement} has been removed :\n") 

def frontItem(arr):
    global front, rear, size
    if(front ==-1):
        print(" ******** Circular-Queue is empty ********")   
    else:
        print("FrontItem : ", arr[front])
def rearItem(arr):
    global front, rear, size
    if(front == -1):
        print(" ******** Circular-Queue is empty ********")   

    else:
        print("realItem : ", arr[rear])    
           

print(" {:*^60s} ".format(" Welcome to Circular Queue Program "))


checkSize = True 
while True:
    if(checkSize): 
        queueSize = int(input("\nEnter size of Queue  : "))
        if(queueSize > 0 ):
            checkSize = False 
            size = queueSize 
            front = -1 
            rear =  -1 
            arr = [ 0  for i in range(queueSize)]

          
        else:
            checkSize = True
            print("\nPlease enter size positive and greater than zero \n")
  
    if(checkSize == False): 

        choice   = int(input("\nEnter you choice Number:\n[1] Enqueue \n[2] Dequeue \n[3] FrontItem \n[4] RearItem \n[5] Exit \n" ))

        if(choice == 1):
            enqueue(arr, input("Enter a element : "))

        elif(choice == 2):
            dequeue(arr)
        elif(choice == 3):
            frontItem(arr)
        elif(choice == 4):
            rearItem(arr)    
        elif(choice == 5):

            print("Thank you for doing some operations \n")  
            break         
        else:
            print("\n******* Invalid  Number *********")     