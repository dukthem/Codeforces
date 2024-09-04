k, r = list(map(int, input().split()))
cnt = 1
ans = 0
while ans == 0:
    # b = cnt*k
    # b = str(b)
    # if b[len(b)-1] == str(r):
    #     ans = 1
    # cnt += 1
    b = cnt * k
    if b % 10 == 0 or b % 10 == r:
        ans = cnt
    if ans != cnt:
        cnt += 1
print(cnt)