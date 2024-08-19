n = int(input())
value = list(map(int, input().split()))
value.sort()
if n == 1:
    print(1)
elif n == 2:
    if value[0] > value[1] or value[1] > value[0]:
        print(1)
    else:
        print(2)
else:
    sum = 0
    for i in range(0, n):
        sum += value[i]
    sum2 = 0
    for i in range(0, n):
        if sum2 < sum:
            sum -= value[i]
            sum2 += value[i]
            if i == n-1:
                print(1)
        else:
            print(len(value)- i + 1)
            break











#sum = 0
#sum2 = 0
#for i in range(0, n):
#    sum += value[i]
#    i += 1
#    for j in range(i, n):
#        sum2 += value[j]
#        print(j)
#    if sum > sum2:
#        print(i)
#        break