n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
s = set()
p[0], q[0] = 0, 0 
pq = p+q
for i in range(len(pq)):
    if pq[i] >0:
        s.add(pq[i])
if len(s) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
