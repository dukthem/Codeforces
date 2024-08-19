t = int(input())
for i in range(0, t):
    n = int(input())
    s = input()
    for j in range(0, len(s)):
        if s[j] == "B":
            cnt = j
            break
    for j in range(len(s)-1, -1, -1):
        if s[j] == "B":
            cnt2 = j

            break
    print((cnt2 - cnt)+1)