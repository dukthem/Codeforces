n = int(input())
a = list(map(int, input().split()))
l = max(a)
cnt = 0
# if n == 1:
#     print(0)
# else:
for i in range(n):
    cnt += (l -  a[i])
print(cnt)