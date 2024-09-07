n = int(input())
s = list(map(int, input().split()))
s.sort(reverse=True)
cnt = 0
for i in range(len(s)):
    if s[i] == 4:
        cnt += 1
    