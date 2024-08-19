s = input()
cnt = 0
for i in range(0, len(s)):
    if s[i] == "7" or s[i] == "4":
        cnt += 1
if cnt == 7 or cnt == 4:
    print("YES")
else:
    print("NO")