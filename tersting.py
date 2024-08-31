n = input()
cnt = 0
for i in range(len(n)):
    if n[i] == n[len(n)-i-1]:
        continue
    else:
        cnt += 1
        break
if cnt==0:
    print("true")
else:
    print("false")