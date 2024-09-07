t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = n
    j = 1
    i = 0
    c = 0
    if(len(a) == 1):
        print("YES")
    else:
        while(i < b-1):
            while(j < b):
                if((a[j]-a[i]) == 1):
                    c = c+1
                elif(a[j] == a[i]):
                    c = c+1
                else:
                    c = c+0
                i = i+1
                j = j+1
 
        if(c == (b-1)):
            print("Yes")
        else:
            print("No")



# t = int(input())
# for i in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     a.sort
#     for j in range(0, n-1):
#         if abs(a[j] - a[j+1]) > 1:
#             print("NO")
#             break
#     else:
#         print("YES")