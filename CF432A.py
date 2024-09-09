n , k = list(map(int,input().split()))
y = list(map(int,input().split()))
y.sort()
cnt = 0
for i in range(len(y)):
    if 5 - y[i] >= k:
        cnt += 1
print(cnt//3)