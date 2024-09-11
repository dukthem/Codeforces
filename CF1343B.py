t = int(input())
for i in range(t):
    k = []
    p = []
    n = int(input())
    cnt = 0
    cnt1 = 0
    if(n % 4 == 0):
        print("YES")
        for j in range(2, n+2, 2):
            cnt += j
            k.append(j)
        for h in range(1, n-2, 2):
            cnt1 += h
            p.append(h)
        n = sum(k) - sum(p)
        p.append(n)
        for m in range(len(p)):
            print(k[m],end=" ")
        for y in range(len(p)):
            print(p[y],end=" ")
    else:
        print("NO")