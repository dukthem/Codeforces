n = int(input())
s = str(n)
if n >= 0:
    print(n)
elif n< 0 and len(s) > 1: 
    if int(s[ :-2]+s[-1])>int(s[:-1]):
        print(int(s[ :-2]+s[-1]))
    else:
        print(int(s[:-1]))
else:
    print(n)