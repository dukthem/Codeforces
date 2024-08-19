nk = list(map(int, input().split()))
for i in range(0, nk[1]):
    if nk[0] % 10 == 0:
        nk[0] = nk[0] // 10
    else:
        nk[0] = nk[0] - 1
print(nk[0])