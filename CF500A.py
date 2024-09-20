n , y = list(map(int,input().split()))
p = list(map(int,input().split()))
x = 1
cnt = 0
while cnt==0:
    x += p[x-1]
    if x == y:
        cnt = 1
        print("YES")
        break
    if x > y:
        cnt = 1
        print("NO")
        break