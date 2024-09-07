t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(set(a))
    cnt = 0
    cnt1 = 0
    for j in range(3):
        if a[j] == b[0]:
            cnt +=1
        else:
            cnt1 += 1
    if cnt <= 1:
        search = b[0]
    else:
        search = b[1]
    for j in range(n):
        if search == a[j]:
            print(j+1)