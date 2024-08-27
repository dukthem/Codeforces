n = int(input())
x = list(map(int, input().split()))
y = []
for i in range(n):
    for j in range(n):
        if x[j] == i+1:
            print(j+1, end=" ")