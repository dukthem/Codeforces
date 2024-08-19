n , m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
sum = 0
for i in range(0, m):
    if a[i] <= 0:
        sum += a[i]
if str(sum)[0] == "-":
    print(str(sum)[1:])
if sum == 0:
    print(sum)