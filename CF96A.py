s = input()
cnt = 0
for i in range (0, len(s)):
    if i < len(s)-1 and s[i] == s[i+1]:
        cnt += 1
        if cnt >= 6:
            print("YES")
            break
    else:
        cnt = 0
if cnt < 6:
    print("NO")