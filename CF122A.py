s = input()
n = int(s)
if n % 4 == 0 or n % 7 == 0 or n % 47 == 0 or n % 74 == 0 or n % 447 == 0 or n % 477 == 0 or n % 444 == 0 or n % 474 == 0 or n % 744 == 0 or n % 747 == 0 or n % 777 == 0 or n % 774 == 0:
    print("YES")
else:
    print("NO")
#cnt = 0
#for i in range(0, len(s)):
 #   if s[i] == "4" or s[i] == "7":
  #      cnt += 1
   #     if cnt == len(s):
    #        print("YES")
     #       if n % i==0:
      #          print("YES")
       #     else:
        #        print("NO")
    #else:
     #   break