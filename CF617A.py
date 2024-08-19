s = int(input())
n1=n2=n3=n4=n5 = 0
m1=m2=m3=m4=m5 = 0
while s != 0:
    if s>=5:
        n1 = s//5
        m1 += n1
        s = s%5
    
    elif s>=4:
        n2 = s//4
        m2 += n2
        s = s%4
    
    
    elif s>=3:
        n3 = s//3
        m3 += n3
        s = s%3
    elif s>=2:
        n4 = s//2
        m4 += n4
        s = s%2
       
    else:
        n5 = s//1
        m5 += n5
        s = s%1
        
print(m1+m2+m3+m4+m5)