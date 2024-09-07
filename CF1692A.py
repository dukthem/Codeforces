t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    cnt = 0
    for j in range(4):
        if a[j] > a[0]:
            cnt += 1
    print(cnt)