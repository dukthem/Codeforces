n = int(input())
cnt_x = 0
cnt_y = 0
cnt_z = 0
for i in range(0, n):
    xyz = list(map(int, input().split()))
    cnt_x = cnt_x + xyz[0]
    cnt_y = cnt_y + xyz[1]
    cnt_z = cnt_z + xyz[2]
if cnt_x == 0 and cnt_y == 0 and cnt_z == 0:
    print("YES")
else:
    print("NO")