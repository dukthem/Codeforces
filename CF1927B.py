t = int(input())
for i in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    A = [['a',0], ['b',0], ['c',0], ['d',0], ['e',0], ['f',0], ['g',0], ['h',0], ['i',0], ['j',0], ['k',0], ['l',0], ['m',0], ['n',0], ['o',0], ['p',0], ['q',0], ['r',0], ['s',0], ['t',0], ['u',0], ['v',0], ['w',0], ['x',0], ['y',0], ['z',0]]
    for j in range(0, len(a)):
        for k in range(0, len(A)):
            if a[j] == A[k][1]:
                A[k][1] += 1
                print(A[k][0], end="")
                break
    print("\n")