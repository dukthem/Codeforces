t = int(input())
for j in range(t):
    score = 0
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(0, (2*n), 2):
        score += min(a[i], a[i+1])
    print(score)