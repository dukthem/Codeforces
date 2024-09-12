n , m , a, b = list(map(int, input().split()))
by_a = n*a # sum by just buying one ticket at a time
s = n // m
cnt = s*b
if n % m == 0:
    if cnt < by_a:
        print(cnt)
    else:
        print(by_a)
else:
    by_r = n % m 
    cnt_1 = cnt
    cnt += by_r * a
    by_x = n+(m - (n%m))
    cnt_1 = (by_x//m) * b 
    z = min(by_a , cnt, cnt_1)
    print(z)