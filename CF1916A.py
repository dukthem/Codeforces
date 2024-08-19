n = int(input())
cnt = 0
for i in range(0 , n):
    a, b = map(int, input().split())
    if a > 1 :
        for i in range(1, b+1):
            if a % i == 0 or b % i == 0:
                cnt += 1
        if cnt ==3:
            print(a*b)
    if a == 1:
        print(b**2)
    