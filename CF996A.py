n = int(input())
ans = 0
cnt = 0
ans = n // 100
n = n % 100
ans += n // 20
n = n % 20
ans += n // 10
n = n % 10
ans += n // 5
n = n % 5
ans += n // 1
print(ans)