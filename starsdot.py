tot=int(input())

for i in range(tot):
    x=input()
    row, col=x.split(" ")
    row=int(row)
    col=int(col)

    for r in range(row):
        st=""
        for c in range(col):
            if r== 0 or r==row-1 or c== 0 or c==col-1:
                st+="*"
            else:
                st+="."
        print(st)
