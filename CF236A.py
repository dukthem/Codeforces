s = input()
a = set()
for i in s:
    a.add(i)

if len(a) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")