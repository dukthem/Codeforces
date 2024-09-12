n = int(input())
x = list(map(int, input().split()))
x.sort()
# print(x)
q = int(input())
for i in range(q):
    m = int(input())
    if m < x[0]:
        print(0)
    elif m >= x[len(x)-1]:
        print(n)
    else:
        ans = 0
        s = 0
        l = n
        cnt = 0
        while ans == 0:   
            for j in range(s, l):
                mid = (l+s) // 2
                if x[mid] > m:
                    l = mid
                    break 
                else:
                    cnt += (l+s)// 2
                    s = mid
                    break
            # for j in range(s, l):
            #     if x[j] <= m:
            #         cnt += 1
            # print(cnt)
            ans = 1
            