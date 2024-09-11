t = int(input())
for i in range(t):
    a = list(map(int,input().split()))
    a.sort(reverse = True)
    if a[0] + a[1] >= 10:
        print("YES")
    else:
        print("NO")