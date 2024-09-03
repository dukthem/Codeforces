n , k = list(map(int, input().split()))
t = 240
a = 0
z = t - k
cnt = 0
for i in range(1,n+1):
    a += 5*i
    if a  <= z:
        cnt += 1
    else:
        break
print(cnt)