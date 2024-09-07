t = int(input())
for i in range(t):
    a, b, c = list(map(int, input().split()))
    if c > a and c > b:
        print("+")
    else:
        print("-")