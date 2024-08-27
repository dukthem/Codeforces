def function(n):
    ans = 0
    # for i in range(1, n+1):
    #     ans += i * (pow(-1, i))
    # even = n* (n + 1)
    # print(even)
    # odd = n * n
    # print(odd)
    # ans = even - odd 
    if n % 2 == 0:
        p = n // 2
        ans += p*(p+1)
        q = n // 2
        ans -= q * q
    else:
        q = (n+1) // 2
        ans -= q*q
        p = (n-1) // 2
        ans += p*(p+1)
    return ans

n = int(input())
function1 = function(n)
print(function1)