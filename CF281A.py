s = input()
if s[0] >= "A" and s[0] <= "Z":
    print(s)
else:
    print(chr(ord(s[0])+ (ord("A") - ord("a"))), end="")
    for i in range(1, len(s)):
        print(s[i], end="")
