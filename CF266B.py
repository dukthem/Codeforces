n , t = list(map(int, input().split()))
s = input()
Y = []
for i in range(n):
    Y.append(s[i])
l = 0
for i in range(t):
    for j in range(l, n):
        if j < n-1 and Y[j] == "B" and Y[j+1] == "G":
            Y[j], Y[j+1] = Y[j+1] , Y[j]
            l = j + 2
        print(Y)
a = str()
for i in range(n):
    a += Y[i]
print(a)