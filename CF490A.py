y = int(input())
z = list(map(int,input().split()))
v = set(z)
one = 0
two = 0
three = 0
if (len(v)!=3):
    print(0)
else:
    for i in range(len(z)):
        if(z[i]==1):
            one += 1
        elif(z[i]==2):
            two += 1
        else:
            three += 1
    p = min(one, two, three)
    a = p
    print(a)
    q = 0
    w = 0
    e = 0
    for j in range(a):
        for l in range(q, len(z)):
            if z[l] == 1:
                print(l+1,end=" ")
                # z = z[:l]+z[l+1:]
                q = l +1
                for y in range(w, len(z)):
                    if z[y]==2:
                        print(y+1,end=" ")
                        # z = z[:y]+z[y+1:]
                        # print(z)
                        w = y +1
                        for g in range(e, len(z)):
                            if z[g]==3:
                                print(g+1)
                                # z = z[:g]+z[g+1:] 
                                # print(z)
                                e = g +1
                                break
                        break
                break