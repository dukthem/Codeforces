a, b = list(map(int , input().split()))
if a == 1 or b == 1:
    if a == 2 or b == 2:
        print(3)
    else:
        print(2)
else:
    print(1)