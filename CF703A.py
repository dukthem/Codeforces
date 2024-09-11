n = int(input())
cm = 0
cc = 0
for i in range(n):
    a , b = list(map(int,input().split()))
    # print (a)
    if a > b:
        cm += 1
    elif b > a :
        cc += 1
    elif b == a :
        continue
if cm > cc:
    print("Mishka")
elif cc > cm :
    print("Chris")
else:
    print("Friendship is magic!^^")