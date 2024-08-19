n = int(input())
row = 0
col = 0
for i in range(0, n):
    a = list(map(int, input().split()))
    for j in range(0, 3):
        if a[j] == 1:
            row = row + 1
    if row >= 2:
        col = col + 1
    row = 0
print(col)