x = list(map(int, input().split()))
x.sort()
l = x[len(x)-1]
c = l - x[0]
a = l - x[len(x)-2]
b = l - (c+a)
print(a, b, c)