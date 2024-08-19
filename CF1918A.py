t = int(input())
for i in range(0, t):
    n, m = map(int, input().split())
    if m % 2 == 0:
        s = m // 2
        print(s*n)
    else:
        s = m-1
        s2 = s//2
        print(s2*n)