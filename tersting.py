# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    positive = []
    negative =[]
    for j in range(len(a)):
        if a[j] <= 0:
            cnt += 1
            negative.append(a[j])
        else:
            positive.append(a[j])
    if cnt %2 == 0:
        print((sum(negative)*-1) + sum(positive))
    else:
        if cnt == 1:
            if (negative[0]*-1) > sum(positive):
                ans =  (negative[0]*-1) - positive[0]
                if len(positive) > 1:
                    ans += + sum(positive)
                    print(ans)
                else:
                    print(ans)
            else:
                print(sum(a))
        else:
            # print(sum(positive) + (sum(negative)*-1) + negative[cnt-1])
            for j in range(cnt):
                if negative[1] <= 0: 
                    negative[0] *= -1
                    negative[1] *= -1
                    negative.sort()
            print(sum(negative) + sum(positive))