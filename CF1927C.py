t = int(input())
for i in range(0, t):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    for j in range(n-1, -1, -1):
        if a[j] > k:
            a = a[:-1]
    for j in range(m-1, -1, -1):
        if b[j] > k:
            b = b[:-1]
    a2 = []
    a2.append(a[0])
    for j in range(0, len(a)):
        if j < len(a)-1 and a[j] != a[j+1]:
            a2.append(a[j+1])
    b2 = []
    b2.append(b[0])
    for j in range(0, len(b)):
        if j < len(b)-1 and b[j] != b[j+1]:
            b2.append(b[j+1])
    ab = a2 + b2
    elem_in_a2 = 0
    comon_elem = 0
    elem_in_b2 = 0
    for j in range(0, len(a2)):
        if j < k+1 and a2[j] == j+1:
            elem_in_a2 += 1
            if j < k+1 and b2[j] == j+1:
                elem_in_a2 -= 1
                comon_elem += 1
        elif j < k+1 and b2[j] == j+1:
            elem_in_b2 += 1
    print(elem_in_a2)
    print(elem_in_b2)
    print(comon_elem)


#    cnt = 0
#    cnt1 = 0
#    for j in range(0, len(a2)):
#        for k in range(0, len(b2)):
#            if a2[j] == b2[k]:
#                cnt += 1
#    
#    if (len(a2) - cnt) + (cnt//2) == k//2:
#        cnt1 += 1
#    if (len(b2) - cnt) + (cnt//2) == k//2:
#        cnt1 += 1
#    if cnt1 == 2:
#        print("YES")
#    else:
#        print("NO")

    
    




#    a2 =[]
#    b2 =[]
#    if n < k//2 or m < k//2:
#        print("NO")
#    else:
#        for i in range(0, n):
#            a2.append(a[i])
#            b2.append(b[i])
#        sum = a2+b2
#        sum.sort()
#        print(sum)