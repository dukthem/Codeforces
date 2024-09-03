n , m = list(map(int, input().split()))
f = list(map(int, input().split()))
f.sort()
# y= []
z = []
# print(f)
# for i in range(n):
#     y.append(f[i])
cnt = 1
ans = 0
cnt2 = 99999
# for i in range(len(f)-1):
#     if f[i] == f[i+1]:
#         cnt += 1
#         if cnt> ans:
#             ans = cnt
#     else:
#         cnt = 1
for i in range(m-n+1):
    ans = f[n-1+i] - f[i]
    cnt2 = min(cnt2, ans)
print(cnt2)
# if ans == n:
#     print(0)
# else:
#     print(y[len(y)-1] - y[0])