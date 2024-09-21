t = int(input())
for i in range(t):
    n = int(input())
    cnt = 0
    ans = 0
    cnt_2 = 0
    cnt_1 = 0
    while ans == 0:
        if n == 1:
            cnt_1 = 1
            ans = 1
            break
        if n % 2 == 0:
            n = n // 2
            if n % 3 == 0:
                n = n // 3
                cnt += 1
        if n % 3 == 0:
            n = n // 3
            if n % 2 == 0:
                n = n // 2
                cnt += 1
        else:
            cnt_2 = 1
            ans = 1
    if cnt_1 == 1:
        print(cnt)
    else:
        print(-1)