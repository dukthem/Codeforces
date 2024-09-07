n = int(input())
a = list(map(int, input().split()))
sreja = 0
dima = 0
for i in range((n//2) +1):
    if len(a) > 1:
        l = max(a[0], a[len(a)-1])
        sreja += l
        a.remove(l)
        s = max(a[0], a[len(a)-1])
        dima += s
        a.remove(s)
    elif len(a) == 1:
        sreja += a[0]
    else:
        break
print(sreja, dima)