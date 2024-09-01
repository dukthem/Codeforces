import math
t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    sqrt_num = math.sqrt(n)
    if sqrt_num.is_integer():
        sqrt_num = int(sqrt_num)
        s = s[sqrt_num: n - sqrt_num]
        cnt = 0
        for i in range(((n-(2*sqrt_num))//sqrt_num)):
            a = s[:sqrt_num]
            s = s[sqrt_num:]
            if a[0] == "1" and a[len(a)-1] == "1" and a[1:len(a)-1] == ("0"*(sqrt_num-2)):
                cnt+=1
        if cnt == sqrt_num-2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")