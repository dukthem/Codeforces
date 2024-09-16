x , y = list(map(int,input().split()))
n = max(x,y)
q = []
for num in range(2,n+1):
    is_prime = True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            is_prime = False
            break
    if is_prime:
        q.append(num)
if y==q[len(q)-1] and x==q[len(q)-2]:
    print("YES")
else:
    print("NO")