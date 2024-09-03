n = int(input())
a = list(map(int, input().split()))
unt = 0
plc = 0
ans = 0
for i in range(n):
    if a[i] <0:
        if plc == 0:
            ans += a[i]
        else:
            plc += a[i]
    else:
        plc += a[i]
    # if a[i] > 0:
    #     plc += a[i]
    #     continue
    # if plc == 0:
    #     unt += (a[i] * -1)
    # elif plc != 0:
    #     plc -= a[i]
    # y = [a[i], plc, unt]
    # print(y)
print(ans*-1)