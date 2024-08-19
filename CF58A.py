s = input()
i = int(0)
x = int(0)
for i in range(len(s)):
    if s[i] == 'h' and x == 0:
        x = 1
        continue
    if s[i] == 'e' and x == 1:
        x = 2
        continue
    if s[i] == 'l' and x == 2:
        x = 3
        continue
    if s[i] == 'l' and x == 3:
        x = 4
        continue
    if s[i] == 'o' and x == 4:
        x = 5
        
if x == 5:
    print('YES')
else:
    print('NO')