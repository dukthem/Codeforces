t = int(input())
for i in range(t):
    n = int(input())
    a  = list(map(int, input().split()))
    ans = 0
    for j in range(1, n+1):
        if j % 2 == 0:
            ans -= a[j-1]
        else:
            ans += a[j-1]
    
    print(ans)