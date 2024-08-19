for i in range(int(input())):
    a=int(input())
    if a & 1:
        print("YES")
    else:
        k=a
        c=0
        while k>2:
            k=k//2
            if (k & 1) and a%k==0:
                c=1
                break
        if c==0:
            print("NO")
        else:
            print("YES")  







#n = int(input())
#cnt= 0
#for i in range(0, n):
#    s = int(input())
 #   if s % 2 != 0:
  #      print("YES")
   # else:
    #    s = s/2
     #   if s%2!=0:
      #      print("YES")
       # else:
        #    print("NO")

  
  
  
  
 
  
  
  
  
  #  for j in range(1, s+1, 2):
   #     
    #    if s%j == 0:
     #       cnt += 1
      #      if cnt > 1:
       ##        cnt = 0
          #      break
        #else:
         #   print("NO")
          #  break