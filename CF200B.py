n = int(input())
v = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += (v[i] / 100)
ans = (ans*100) / n
print(f"{ans: .4f}")