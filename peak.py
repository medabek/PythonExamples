n = int(input())
arr1 = list(map(int, input().split()))

##########First Iterative way
def funcPeak(arr):
     for i in range(0, len(arr)):
          if (i == 0 and arr[i]>=arr[i+1]):
               return(arr[i])
          elif (i == len(arr)-1 and arr[i] >= arr[i-1]):
               return(arr[i])
          elif (arr[i]>=arr[i-1] and arr[i]>=arr[i+1]):
               return(arr[i])

#print(funcPeak(arr1))



###########Second Recursive way
import sys

def findPeak(arr, low, high, n): 

     mid = len(arr)/2 
     mid = int(mid)

     if(arr[0]>=arr[1]):
          return arr[0]

     elif ((mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid])):
          return  arr[mid]
     

     elif (mid > 0 and arr[mid - 1] > arr[mid]): 
         return findPeak(arr, low, (mid - 1), n) 
  

     else: 
         return findPeak(arr, (mid + 1), high, n)



print(findPeak(arr1, low=0, high=len(arr1)-1, n=len(arr1)))
