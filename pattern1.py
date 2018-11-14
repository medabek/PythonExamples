tot=int(input())

for i in range(tot):
    x=input()
    row, col=x.split(" ")
    row=int(row)
    col=int(col)

    for r in range(row):
        st=""
        for c in range(col):
            if (r+c)%2==0:
                st+="*"
            else:
                st+="."
        print(st)
