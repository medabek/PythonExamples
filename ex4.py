num=int(input())
for i in range(num):
    nums=input()
    n, x, y=nums.split(" ")
    n=int(n)
    x=int(x)
    y=int(y)

    for i in range(1, n):
        if i%x==0 and i%y!=0:
            print(i, end=" ")
    print()
    
