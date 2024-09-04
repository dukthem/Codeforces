n, k, l, c, d, p, nl, np = list(map(int, input().split()))
friend = n
bottle = k
liter_perbottle = l
total_liters = k*l
limes = c
slice = d
total_slice = c*d
salt = p
y = [total_liters//nl, total_slice, salt//np]
y.sort()
print(y[0]//n)