t = int(input())
for i in range(t):
    n = int(input())
    if n % 4 == 0:
        print(n // 4)
    else:
        ans = n // 4
        ans2 = (n%4) // 2
        print(ans + ans2)