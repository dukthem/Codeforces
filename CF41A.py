s = input()
t = input()
cnt = 0
if len(s) == len(t):
    for i in range(0, len(s)):
        if s[i] == t[len(s)-i-1]:
            cnt += 1
    if cnt == len(s):
        print("YES")
    else:
        print("NO")
else:
    print("NO")