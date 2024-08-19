a = int(input())
b = int(input())
c = int(input())
test1 = a+b*c
test2 = a*(b+c)
test3 = a*b*c
test4 = (a+b)*c
test5 = a+b+c
test6 = a*b+c
test7 = (a*b)+c
test8 = a+(b*c)
ans = max(test1, test2, test3, test4, test5, test6, test7, test8)
print(ans)
#if a == 1 or b == 1 or c == 1:
 #   ar = [a,b,c]
  #  ar.sort()
   # print((ar[0]+ar[1])*ar[2])
#else:
 #   print(a*b*c)