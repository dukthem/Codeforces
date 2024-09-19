def find_between(lst, num):
    low, high = 0, len(lst)-1
    if num < lst[low]  or num > lst[high]:
        return None
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == num:
            return mid, mid
        elif lst[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    return high, low
    
n = int(input())
x = list(map(int, input().split()))
x.sort()
q = int(input())
for i in range(q):
    m = int(input())
    if m < x[0]:
        print(0)
    elif m >= x[len(x)-1]:
        print(n)
    else:
        result = find_between(x, m)
        cnt = result[0]+1
        
        if x[result[0] + 1] <= m:
            while x[result[0]+1] <= m:
                cnt += 1
            print(cnt)
        else:
            print(cnt)
        
        
        # ans = 0
        # s = 0
        # l = n
        # cnt = 0
        # while ans == 0:   
        #     for j in range(s, l):
        #         mid = (l+s) // 2
        #         if x[mid] > m:
        #             l = mid
        #             break 
        #         else:
        #             cnt += (l+s)// 2
        #             s = mid
        #             break
        #     # for j in range(s, l):
        #     #     if x[j] <= m:
        #     #         cnt += 1
        #     # print(cnt)
        #     ans = 1
            