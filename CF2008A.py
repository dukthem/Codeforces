t = int(input())
for i in range(t):
    a, b = list(map(int, input().split()))
    if a  == 0 and b > 0:
        if b % 2 == 0:
            print("YES")
        else:
            print("NO")
    elif a == 0 and b == 0:
        print('YES')
    elif a > 0 and b == 0:
        if a % 2 == 0:
            print("YES")
        else:
            print("NO")
    elif a % 2 == 0 and b % 2 == 0:
        print("YES")
    elif a % 2 == 0 and b % 2 != 0:
        print("YES")
    elif a % 2 != 0 and b % 2 == 0:
        print("NO")
    else:
        print("NO")
    