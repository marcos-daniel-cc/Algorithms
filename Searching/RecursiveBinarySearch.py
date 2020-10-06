
def recursiveBinarySearch (array, left, right, x): 
     
  if right >= left: 
  
    middle = left + (right - left) // 2
  
        
    if array[middle] == x: 
      return middle 

    elif array[middle] > x: 
      return recursiveBinarySearch(array, left, middle-1, x) 
  
    else: 
      return recursiveBinarySearch(array, middle + 1, right, x) 
  
  else: 
    return -1

array = [ 23, 334, 50, 68, 104, 360, 500 ] 
x = 360
  
 
index = recursiveBinarySearch(array, 0, len(array)-1, x) 
  
if index != -1: 
  print ("Element is present at index % d" % index) 
else: 
  print ("Element is not present in array") 