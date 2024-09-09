n = int(input())
s = list(map(int, input().split()))
s.sort(reverse=True)
ans = 0
c4 = 0
c3 = 0
c2 = 0
c1 = 0
for i in range(len(s)):
    if s[i] == 4:
        c4 += 1
    elif s[i] ==3:
        c3 += 1
    elif s[i] == 2:
        c2 += 1
    else:
        c1 += 1
ans += c4
ans += c3
if c3 >= c1:
    c1 = 0
else:
    c1 -= c3
ans += c2//2
c2 = c2 % 2
if c2 > 0 and c1 == 0:
    ans += 1
elif c2 == 0 and c1 > 0:
    ans += c1//4
    c1 = c1 % 4
    if c1 > 0:
        ans += 1
elif c2 > 0 and c1 >0:
    if c1 <= 2:
        ans += 1 
    else:
        ans += 1
        c1 -= 2
        ans += c1//4
        c1 = c1 % 4
        if c1 > 0:
            ans += 1
        
print(ans)









# cnt = 0
# for i in range(len(s)):
#         if s[i] == 4:
#             cnt += 1
#         else:
#             s = s[i:]
#             break
# print(s)
# while len(s) > 0:
#     for i in range(len(s)):
#         if (s[i] == 3 and s[len(s)-1] == 1):
#             cnt += 1
#             s = s[1:len(s)-1]
#             break
#         elif (s[i] == 3 and s[len(s)-1] != 1):
#             cnt += 1
#             s = s[1:]
#             break
#         if i < len(s)-1 and s[i] == 2 and s[i+1] == 2:
#             cnt += 1
#             s[2: len(s)]
#             break
        