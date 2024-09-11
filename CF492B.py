n , l = list(map(int, input().split()))
a = list(map(int, input().split()))
# a.append(0)
a.sort()
lar = 0
if a[0] == 0 and a[len(a)-1] == l:
    for i in range(len(a)):
        if i < len(a)-1:
            dif = abs((a[i] - a[i+1])/2)
        lar = max(dif, lar)
    print(f"{lar:.9f}")
else:
    a.append(0)
    a.sort()
    for i in range(len(a)):    
        if i < len(a)-1:
            dif = abs((a[i] - a[i+1])/2)
            if a[i] == 0:
                dif = dif*2
        lar = max(dif, lar)
    if a[len(a)-1] == l:
        print(f"{lar:.9f}")
    else:
        dif = abs(a[len(a)-1] - l)
        lar = max(dif, lar)
        print(f"{lar:.9f}")