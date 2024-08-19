n, m = map(int, input().split())
for i in range(0, max(n, m)):
    n -= 1
    m -= 1
    if n*m == 0:
        break
if i == 0 or i % 2 == 0:
    print("Akshat")
else:
    print("Malvika")