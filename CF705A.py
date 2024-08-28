n = int(input())
ans = "I hate"
for i in range(2, n+1):
    if i % 2 != 0 :
        ans += " that I hate"
    elif i % 2 == 0:
        ans += " that I love"
ans += " it"
print(ans)
        