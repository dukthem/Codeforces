t = int(input())
for i in range(0, t):
    ans = 0
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for j in range(0, n):
        if j < n -1:
            b = a[j+1] - a[j]
            ans += b
    print(ans)