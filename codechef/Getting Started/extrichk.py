a,b,c=input().split()
a,b,c=int(a),int(b),int(c)
if (a+b>c) and (a+c>b) and (b+c>a):
    if (a==b) and (b==c):
        print('1')
    elif (a==b) or (a==c) or (b==c):
        print('2')
    if (a!=b) and (a!=c) and (b!=c):
        print('3')
else:
    print('-1')