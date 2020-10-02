def mergeSort(array): 
    if len(array) >1: 
        mid = len(array)//2 
        leftArray = array[:mid] 
        rightArray = array[mid:]
  
        mergeSort(leftArray)
        mergeSort(rightArray) 
  
        i = 0
        j = 0
        k = 0
          
      
        while i < len( leftArray) and j < len(rightArray): 
            if  leftArray[i] < rightArray[j]: 
                array[k] =  leftArray[i] 
                i+= 1
            else: 
                array[k] = rightArray[j] 
                j+= 1
            k+= 1
          
        while i < len(leftArray): 
            array[k] =  leftArray[i] 
            i+= 1
            k+= 1
          
        while j < len(rightArray): 
            array[k] = rightArray[j] 
            j+= 1
            k+= 1
  

def printArray(array): 
    for i in range(len(array)):         
        print(array[i], end =" ") 
    print() 

array = [4,65,3334,23,34,566,96,70,3,43,72,945]  
print ("Original Array:", end ="\n")  
printArray(array) 
mergeSort(array) 
print("Sorted Array:", end ="\n") 
printArray(array) 
  
 