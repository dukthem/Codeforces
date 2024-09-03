t = int(input())
for i in range(t):
    a, b = list(map(int, input().split()))
    ans = 100
    for c in range(a, b+1):
        ans =  min(ans, (c - a) + (b - c))
    print(ans)