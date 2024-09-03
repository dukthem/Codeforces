t = int(input())
for i in range(t):
    n = int(input())
    y = []
    for j in range(n):
        a = input()
        for k in range(4):
            if a[k] == "#":
                y.append(k+1)
    for j in range(len(y)-1,-1,-1):
        print(y[j], end=" ")