n , m = list(map(int, input().split()))
a = list(map(int, input().split()))
cnt = 0
for i in range(len(a)):
    if i == 0:
        cnt = a[0]-1
    if i < len(a)-1 and a[i] < a[i+1]:
        cnt += (a[i+1] - a[i])
    elif i < len(a)-1 and a[i] == a[i+1]:
        cnt += 0
    elif i < len(a)-1 and a[i] > a[i+1]:
        cnt += ((n-a[i]) + (a[i+1]))
print(cnt)