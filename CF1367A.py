t = int(input())
for i in range(t):
    l = []
    z = input()
    m = 0
    cnt = 1
    while cnt <= len(z):
        for j in range(m, len(z)):
            if j == 0 or j == len(z)-1:
                print(z[j], end="")
                cnt += 1
            else:
                print(z[j], end="")
                m = j +2
                cnt += 2
                break
    print("")