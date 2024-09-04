a, b = list(map(int, input().split()))
c = min(a,b)
print(c, end=" ")
a -= c
b -= c
d = max(a,b)
print(d//2)