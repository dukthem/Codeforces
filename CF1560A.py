t = int(input())
y = []
for i in range(t):
    a = int(input())
    y.append(a)
l = max(y)
s = []
for i in range(1, l*100):
    n = str(i)
    if i % 3 != 0 and n[len(n)-1] != "3":
        s.append(i)
for i in range(t):
    print(s[y[i]-1])