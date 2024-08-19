n = int(input())
a = list(map(int, input().split()))
ans = 1
cnt = 1
for i in range(0, n):
    if i < n-1 and a[i+1] >= a[i]:
        cnt = cnt + 1
    else:
        cnt = 1
    ans = max(ans, cnt)

print(ans)