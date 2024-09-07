t = int(input())
for i in range(t):
    n = (input())
    y = [int(n[0]), int(n[1]), int(n[2])]
    z = [int(n[len(n)-1]), int(n[len(n)-2]), int(n[len(n)-3])]
    if sum(y) == sum(z):
        print("YES")
    else:
        print("NO")