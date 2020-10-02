
 
def partition(array, low, high):
    i = (low-1)        
    pivot = array[high]    
 
    for j in range(low, high):

        if array[j] <= pivot:
            i = i+1
            array[i], array[j] = array[j], array[i]
 
    array[i+1], array[high] = array[high], array[i+1]
    
    return (i+1)
 

 
 
def quickSort(array, low, high):
    if len(array) == 1:
        return array
    if low < high:
 
        pi = partition(array, low, high)
        quickSort(array, low, pi-1)
        quickSort(array, pi+1, high)
 



array = [800, 234, 89, 34, 1, 5, 5, 2, 4, 8, 23, 34, 3, 9, 7]
n = len(array)
quickSort(array, 0, n-1)
print("Result clasical quicksort algorithm:")
for i in range(n):
    print("%d" % array[i]),
 
