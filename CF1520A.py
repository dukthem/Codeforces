t = int(input())
for i in range(t):
    cnt = 0
    n = int(input())
    x = input()
    for j in range(0,len(x)):
        if j<len(x)-1 and x[j]==x[j+1]:
            continue
        else:
            for g in range(j+1,len(x)):
                if x[j] == x[g]:
                    cnt += 1
                    break
        if cnt == 1:
            print("NO")
            break
    if cnt == 0:
        print("YES")