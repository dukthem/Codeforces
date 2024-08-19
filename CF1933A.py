t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for j in range(0, n):
        if a[j] >= 0:
            cnt += a[j]
        else:
            a[j] = a[j] * -1
            cnt += a[j]
    print(cnt)