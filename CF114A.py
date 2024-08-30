# n = int(input())
# a = list(map(int, input().split()))
# in_lar = 0
# in_sam = 0
# steps = 0
# for i in range(n):
#     if a[i] == max(a) and in_lar < 0:
#         in_lar = i
#     elif a[i] == min(a):
#         in_sam = i
# if in_lar > in_sam:
#     print(in_lar + (n -1) -in_sam -1)
# else:
#     print(in_lar + (n-1) - in_sam)
n = int(input())
a = list(map(int, input().split()))
lar = 0
sam = 0
for i in range(n):
    if a[i] == min(a):
        sam = i+1  
for i in range(n-1, -1, -1):
    if a[i] == max(a):
        lar = i+1  
if lar > sam:
    print((lar-1) + (n - sam) -1)
else:
    print((lar-1) + (n - sam))