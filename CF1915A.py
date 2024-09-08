t = int(input())
for i in range(t):
    a, b, c = list(map(int, input().split()))
    if a == b:
        print(c)
    elif a == c:
        print(b)
    elif c == b:
        print(a)
    