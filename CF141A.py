a=input()
b=input()
c=input()
d=a+b
z=[]
x=[]
for i in range(len(d)):
    z.append(d[i])
z.sort()
for i in range(len(c)):
    x.append(c[i])
x.sort()
cout=0
if len(x) != len(z):
    print("NO")
else:
    for i in range(len(x)):
        if(x[i]==z[i]):
            cout+=1
    if(cout==len(x)):
        print("YES")
    else:
        print("NO")