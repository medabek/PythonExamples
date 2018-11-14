x=int(input())
arr = list(map(int, input().strip().split(' ')))
for i in range(1,len(arr)):
    for j in range(0, i):
        if arr[j]>arr[i]:
            arr[i], arr[j] = arr[j], arr[i]
print("Iterative way: " ,arr)


# Recursive Bubble sort 
  
def bubble_sort(listt, n):
    if (n<2):
        return listt
    for i in range(n-1):
        if (listt[i]>listt[i+1]):
            listt[i], listt[i+1] = listt[i+1], listt[i]
            
    return bubble_sort(listt, n-1)
print("Recursive way: ", bubble_sort(arr, len(arr)))
