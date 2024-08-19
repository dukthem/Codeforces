a = list(map(int, input().split()))
i = 0
while a[0]<= a[1]:
    a[0] = a[0] * 3
    a[1] = a[1] * 2
    i += 1
print(i)