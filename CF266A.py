n = int(input())
s = input()
cnt = 0
for i in range(0, n):
    if i < n-1 and s[i] == s[i+1]:
        cnt += 1
print(cnt)