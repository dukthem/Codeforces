n , m = list(map(int, input().split()))
a = True
for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            print("#", end="")
        else:
            if  a == True:
                print("."*(m-1), end="")
                print("#", end="")
                a = False
                break
            else:
                print("#", end="")
                print("."*(m-1), end="")
                a = True
                break
    print("")