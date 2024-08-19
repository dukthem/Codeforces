s = input()
n = len(s)
ref = "WUB"
cnt = 343
i = 0
ans = ""
while(i < n):
    if i < n-2 and s[i : (i+3)] == ref:
        cnt = cnt + 1
        i = i + 3
        if cnt == 1:
            ans = ans + " "
    else:
        ans = ans + s[i]
        i = i + 1
        cnt = 0

if ans[-1] == " ":
    print(ans[:-1])
else:
    print(ans)
