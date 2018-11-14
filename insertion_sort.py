# Function to do insertion sort 
def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            #print (j)
            j -= 1
            #print(j)
        arr[j+1] = key
    return arr

arr = [12, 11, 13, 5, 6, 7]
print("Iterative way " ,insertionSort(arr))



def insertionSortRecursive(arr,n): 
    # base case 
    if n<=1: 
        return
      
    # Sort first n-1 elements 
    insertionSortRecursive(arr,n-1) 

    last = arr[n-1] 
    j = n-2 
    while (j>=0 and arr[j]>last): 
        arr[j+1] = arr[j] 
        j = j-1
  
    arr[j+1]=last
    return arr

arr = [12, 11, 13, 5, 6, 7]
print("Recursive way " ,insertionSortRecursive(arr, len(arr)))
