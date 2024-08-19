s = input()
cnt = 0
for i in range(0, len(s)):
    if ord(s[i]) == ord("H") or ord(s[i]) == ord("Q") or ord(s[i]) == ord("9"):
        cnt += 1
        break
if cnt > 0:
    print("YES")
else:
    print("NO")