s = input()
cnt2 = 0
cnt = 0
if ord(s[0]) < ord("a"):
    for i in range(0, len(s)):
        if ord(s[i]) < ord("a"):
            cnt += 1
    if cnt == len(s):
        for i in range(0, len(s)):
            print(chr(ord(s[i])+ (ord("a") - ord("A"))), end="")
    else:
        print(s)
else:
    for i in range(0, len(s)):
        if ord(s[i]) < ord("a"):
            cnt2 += 1
    if cnt2 == len(s)-1:
        print(chr(ord(s[0])+ (ord("A") - ord("a"))), end="")
        for i in range(1, len(s)):
            print(chr(ord(s[i])+ (ord("a") - ord("A"))), end="")
    else:
        print(s)