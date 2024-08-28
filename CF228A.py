n = list(map(int, input().split()))
s = set()
for i in range(len(n)):
    s.add(n[i])
print(4 - len(s))