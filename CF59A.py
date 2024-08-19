s = input()
up = 0
low = 0
for i in range(0, len(s)):
    if ord(s[i]) < ord("a"):
        up += 1
    if ord(s[i]) > ord("Z"):
        low += 1
if up <= low:
    for i in range(0, len(s)):
        if ord(s[i]) > ord("Z"):
            print(s[i], end="")
        else:
            print(chr(ord(s[i])+ (ord("a") - ord("A"))), end="")
else:
    for i in range(0, len(s)):
        if ord(s[i]) < ord('a'):
            print(s[i], end="")
        else:
            print(chr(ord(s[i]) - (ord("a") - ord("A"))), end="")