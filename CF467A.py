n = int(input())
cnt = 0
for i in range(n):
    p ,q = list(map(int, input().split()))
    if q >= p+2:
        cnt += 1
print(cnt)