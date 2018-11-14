num=int(input())
arr1=[]
arr2=[]
for i in range(num):
    n = int(input())
    arr = [int(x) for x in input().split()]
    for a in range(len(arr)//2):
        arr1.append(arr[a])
    for a in range(len(arr)//2, len(arr)):
        arr2.append(arr[a])
    for i in range((len(arr))//2):
        print(arr1[i], arr2[i], end=" ")
    print()
    arr1=[]
    arr2=[]
        

