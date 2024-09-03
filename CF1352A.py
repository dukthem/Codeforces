t = int(input())
for i in range(t):
    n = input()
    l = 0
    y = []
    for j in range(len(n)-1, -1, -1 ):
        # for k in range()
        for k in range(l ,len(n)):
            if n[k] != "0":
                y.append(n[k]+("0"*j))
            l += 1
            break
    print(len(y))
    for j in range(len(y)):
        print(y[j], end=" ")
    print("")