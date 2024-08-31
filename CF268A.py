n = int(input())
y = []
for i in range (n):
    ha = list(map(int, input().split()))
    game = n *(n-1)
    y.append(ha)
cnt = 0
for i in range(n):
    for j in range(n):
        if y[i][0] == y[j][1]:
            cnt += 1
print(cnt)