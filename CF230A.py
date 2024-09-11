s, n = list(map(int, input().split()))
y = []
cnt = 0
for i in range(n):
    xy = list(map(int, input().split()))
    y.append(xy)
y.sort()
for i in range(len(y)):
    if y[i][0] >= s:
        print("NO")
        cnt += 1
        break
    else:
        s += y[i][1]
if cnt == 0:
    print("YES")