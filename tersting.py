# cook your dish here
t = int(input())
for i in range(t):
    n , k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    # for j in range(k):
    #     l = a[0] + a[len(a)-1]
    #     a = a[1:len(a)-1]
    #     a.append(l)
    y = a[:k]
    x = sum(y)
    l = x + a[len(a)-1]
    for j in range(k, len(a)-1):
        print(a[j], end =" ")
    print(l, end=" ")    
    print("")