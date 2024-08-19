nk = list(map(int, input().split()))
row = list(map(int, input().split()))
col = 0
if row[nk[1]-1] == 0:
        if row[0] == 0:
            print(0)
        else:
            for j in range(0, nk[0]):
                if row[j] > 0:
                    col = col+1
            print(col)
else:
    for i in range(0, nk[0]):
        if row[i] >= row[nk[1]-1]:
            col = col+1
    print(col)