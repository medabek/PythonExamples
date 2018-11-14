x=int(input())
S = list(map(int, input().strip().split(' ')))
n=int(input())
Q = list(map(int, input().strip().split(' ')))
newarr = []
for i in S:
    if i not in Q:
        newarr.append(i)
print(newarr)
