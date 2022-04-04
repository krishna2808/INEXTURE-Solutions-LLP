
def rearrange_array(lst, size):
   print('orignal List     : ', lst)
   
   
   print('orignal List     : ', lst)
   lst += lst
   for index  in range(size):
      lst[lst[index] + size] = index
   print("\nRearrange Array  : ",  lst[size:] )   
  

   
         


# --- Code starting from this point and input validation  

count, inserted, lst  = 0, False, [] 
size = input("\nEnter size of list : ")
if(size.isnumeric()):
   size = int(size)
   while(count < size):
      element = input(f"Enter {count+1} Element : ")
      if(element.isnumeric()):
         element = int(element)
         if(element < size):
            if(element not in lst):
               lst.append(element)
               count +=  1 
               if(count == size):
                  inserted = True
            else:
                print('\nDuplication element is not Allow ')      
         else:
             print("\nElement should be less than size of list ")     

      else:   
         print("\nEnter valid Number  ")

else:
    print("Enter valid size of List ")


if(inserted):
   rearrange_array(lst, size)
