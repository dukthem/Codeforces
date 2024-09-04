n = int(input())
a = list(map(int, input().split()))
c = a[0]
cnt = 0
for i in range(1,len(a)):
    for j in range(i):
        if a[i] > max(c, a[j]):
            cnt += 1
        c = max(c, a[i])
c = a[0]
for i in range(1,len(a)):
    for j in range(i):
        if a[i] < min(c, a[j]):
            cnt += 1
        c = min(c, a[i])
print(cnt)