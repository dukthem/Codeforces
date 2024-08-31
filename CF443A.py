n = input()
s = set()
if n != "{}":
    for i in range(1, len(n)-1, 3):
        s.add(n[i])
print(len(s))
    