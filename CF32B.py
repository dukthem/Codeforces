a = input()
l = 0
ans = 0
cnt = 0
while ans == 0:
    for i in range(l, len(a)):
        if a[i] == ".":
            print(0, end="")
            cnt += 1
        else:
            if i < len(a)-1 and a[i+1] == ".":
                print(1, end="")
                l = i+2
                cnt += 2
                break
            elif i < len(a)-1 and a[i+1] == "-":
                print(2, end ="")
                l = i+2
                cnt += 2
                break
    if cnt == len(a) :
        ans = 1