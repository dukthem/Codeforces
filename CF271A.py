n = int(input())
s = set()
ans = 0
while ans == 0:
    n += 1
    a = str(n)
    for i in range(len(a)):
        s.add(a[i])
    if len(s) == len(a):
        print(n)
        break
    else:
        s.clear()




# import math
# n = int(input())
# ans = 0
# cnt= 0
# while ans == 0:
#     n += 1
#     a = str(n)
# #    no_of_comb = ((math.factorial(len(a)))//(math.factorial(len(a)-2)*math.factorial(2)))
#     for i in range(0, len(a)-1):
#         for j in range(i+1, len(a)):
#             if a[i] == a[j]:
#                 cnt += 1
                
#                 #if cnt == no_of_comb:
#                  #   ans = n
#                   #  print(n)
#                    # break
#     if cnt == 0:
#         ans = n
#         break
# print(ans)
# #            elif a[i] != a[j] and i == len(a)-2 and j == len(a)-1:
#  #               ans = n
#   #              break
# #print(ans)