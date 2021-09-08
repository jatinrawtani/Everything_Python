# s = (a + b + c)/2
# A = √[s(s-a)(s-b)(s-c)]
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if (a+b>c) and (b+c>a) and (a+c>b):
    print('YES')
else:
    print('NO')