n = int(input())
s = input()
cnt_A = 0
cnt_D = 0
for i in range(0, n):
    if s[i] == "A":
        cnt_A += 1
    else:
        cnt_D += 1
if cnt_A > cnt_D:
    print("Anton")
elif cnt_D > cnt_A:
    print("Danik")
else:
    print("Friendship")