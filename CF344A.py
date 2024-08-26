n = int(input())
y = []
for i in range(n):
    x = int(input())
    y.append(x)
cnt = 1
for i in range(n):
    if i<n-1 and y[i] != y[i+1]:
        cnt += 1
print(cnt)