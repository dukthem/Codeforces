import math
t = int(input())
for i in range(t):
    n = int(input())
    x, y = list(map(int, input().split()))
    s = min(x, y)
    print(math.ceil(n/s))