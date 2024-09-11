x , y = list(map(int,input().split()))
c = max(x,y)
d = 7-c
if d == 2:
    print("1/3")
elif d == 3:
    print("1/2")
elif d == 4:
    print("2/3")
elif d == 5:
    print("5/6")
elif d == 6:
    print("1/1")
else:
    print("1/6")