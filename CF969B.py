t = int(input())
for i in range(t):
    n , m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    for j in range(m):
        op = list(map(str, input().split()))
        #op[0] = sign
        #op[1] = l
        #op[2] = r
        for k in range(n):
            if op[0] == "+":
                if int(op[1]) <= a[k] <= int(op[2]):
                    a[k] += 1
            else:
                if int(op[1]) <= a[k] <= int(op[2]):
                    a[k] -= 1
        print(max(a), end=" ")
    print("")