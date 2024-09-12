a = list(map(int,input().split()))
z = (input())
ans = 0
for i in range(len(z)):
    ans += a[int(z[i])-1]
print(ans)
