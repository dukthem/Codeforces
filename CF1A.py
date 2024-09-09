import math
n , m , a = list(map(int, input().split()))
tiles = (n*m) // (a*a)
ar_fl = n*m
ar_ti = a*a
if n <= a and m <= a:
    print(1)
elif n > a and m <= a:
    print(math.ceil(n/a))
elif n < a and m >= a:
    print(math.ceil(m/a))
else:
    if ar_fl % ar_ti == 0 and n%a ==0 and m % a== 0:
        print(tiles)
    else:
        print(math.ceil((n/a))*math.ceil(m/a))