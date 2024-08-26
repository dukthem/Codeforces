n = int(input())
s = list(map(int, input().split()))
cnt_H = 0
for i in range(n):
    if s[i] == 1:
        cnt_H += 1
if cnt_H > 0:
    print("HARD")
else:
    print("EASY")