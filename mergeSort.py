# Python program for implementation of MergeSort 
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        Leftarray = arr[:mid] # Dividing the array elements  
        Rightarray = arr[mid:] # into 2 halves 
  
        mergeSort(Leftarray) # Sorting the first half 
        mergeSort(Rightarray) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(Leftarray) and j < len(Rightarray): 
            if Leftarray[i] < Rightarray[j]: 
                arr[k] = Leftarray[i] 
                i+=1
            else: 
                arr[k] = Rightarray[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(Leftarray): 
            arr[k] = Leftarray[i] 
            i+=1
            k+=1
          
        while j < len(Rightarray): 
            arr[k] = Rightarray[j] 
            j+=1
            k+=1
        return arr

arr = [12, 11, 1, 5, 0, 2, 100, 3, 5, 6, 7]
print("Iterative way " ,mergeSort(arr))


def merge(left, right):
    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    #print(result, "here")
    return result


def merge_sort(array):
    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    return merge(left, right)

arr = [12, 11, 13, 5, 6, 7]
print("Recursive way " ,merge_sort(arr))





def merge_Sort(a):
    mergeSort2(a, 0,len(a)-1)

def mergeSort2(a, first, last):
    if first<last:
        middle=(first+last)//2
        #print(middle)
        mergeSort2(a, first, middle-1)
        mergeSort2(a, middle, last-1)
        merge(a, first, middle, last)
    return a

def merge(a, first, middle, last):
    l = a[:middle]
    r = a[middle+1:]
    print(l, r)
    i = j = 0
    for k in range(first, last+1):
        if l[i]<=r[j]:
            a[k]=l[i]
            i+=1
        else:
            a[k]=r[j]
            j+=1
    return a
print("Second rec merge ", mergeSort2(arr, 0, len(arr)-1)) 
