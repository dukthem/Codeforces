t = int(input())
for i in range(t):
    a, b = list(map(int, input().split()))
    cnt = 0
    ans = abs(a - b)
    cnt = ans // 10
    if ans % 10 != 0:
        cnt += 1
    # while ans == -1:
    #     if a == b:
    #         ans = 0
    #     elif a < b:
    #         while ans == -1:
    #             a += 10
    #             cnt += 1
    #             if a >= b:
    #                 ans = cnt
    #     else:
    #         while ans == -1:
    #             a -= 10
    #             cnt += 1
    #             if a <= b:
    #                 ans = cnt
    print(cnt)