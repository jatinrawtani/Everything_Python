a,b,c=input().split()
a,b,c=int(a),int(b),int(c)
if (a+b>c or a+c>b or b+c>a) and a+b+c==180 and (a>0 and b>0 and c>0):
    print('YES')
else:
    print('NO')