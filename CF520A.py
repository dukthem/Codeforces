n = int(input())
a  = input()
s = set()
for i in range(n):
    s.add(a[i])
if len(s) >= 26:
    print("YES")
else:
    print("NO")