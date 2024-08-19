a = 0
b = 0
stepr = 0
stepc = 0
for i in range(0, 5):
    n = list(map(int, input().split()))
    a += 1
    for j in range(0, 5):
        b += 1
        if n[j] == 1:
            if a <= 3:
                stepr = 3 - a
            else:
                stepr = a - 3
        if n[j] == 1:
            if b <= 3:
                stepc = 3 - b
            else:
                stepc = b - 3
    b = 0
print(stepr+stepc)