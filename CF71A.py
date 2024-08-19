n = int(input())
for i in range(n):
    a = input()
    if len(a) > 10:
        print(a[0], end="")
        print(len(a)-2, end="")
        print(a[len(a)-1])
    else:
        print(a)