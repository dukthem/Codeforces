t = int(input())
for i in range(t):
    n, m, q = list(map(int, input().split()))
    b = sorted(list(map(int, input().split())))
    a = list(map(int, input().split()))
    # for j in range()
    if a < b[0]:
        print(b[0]-1)
    elif a > b[1]:
        print(n-b[1])
    else:
        s = b[1] - b[0] - 1
        if s % 2 == 0:
            print(s//2)
        else:
            print((s+1)// 2)