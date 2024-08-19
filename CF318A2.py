n, k = map(int, input().split())
if n % 2 == 0:
    if n//2 >= k:
        print(1 + (2*(k-1)))
    else:
        print(2 + (2*(k-(n//2)-1)))
else:
    if (n//2) + 1 >= k:
        print(1 + (2*(k-1)))
    else:
        print(2 + (2*(k-(n//2 + 1) - 1)))
#if n % 2 == 0:
 #   if k <= n//2:
  #      cnt = 0
   #     trail = 1
    #else:
    #    cnt = n//2
     #   trail = 2
#else:
 #   if k <= (n//2)+1:
  #      cnt = 0
   #     trail = 1
    #else:
     #   cnt = (n//2)+1
      #  trail = 2
    
#for i in range(trail, n, 2):
 #   cnt += 1
  #  if k == cnt:
   #     print(i)
###print(trail + ((k-1)*2))