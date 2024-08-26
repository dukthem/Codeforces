n , t = list(map(int, input().split()))
s = input()
for i in range(t):
    if i < t-1 and s[i] == "B" and s[i+1] == "G":
        s[i], s[i+1] = s[i+1] , s[i]
print(s)