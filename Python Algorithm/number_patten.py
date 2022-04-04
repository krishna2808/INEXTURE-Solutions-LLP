
'''

1    2    3    4
12   13   14   5
11   16   15   6
10   9    8    7

'''




while(True):
  num = input("\nEnter you number of rows : ")
  if(num.isnumeric()):
    num = int(num)
    number  = 1
    low = 0 
    high = num-1
    number_list = [  [ 0 for j in range(num)] for i in range(num)]
  	# print(number_list)

    count = int((num+1)/2)

    for i in range(count):
      for j in  range(low, high+1):
        number_list[i][j] = number 
        number +=  1 
      for j in range(low+1 , high+1 ):
          number_list[j][high] = number
          number += 1 
      for j in range(high-1 , low -1  , -1):
          number_list[high][j] = number
          number += 1 
      for j in range(high -1, low, -1):
          number_list[j][low] = number 
          number += 1 
      low += 1
      high -= 1
    print()
    for i in range(num):
        for j in range(num):
          print(number_list[i][j], end="\t")
        print()		
    break    
  else:
      print("Invalid Input")      