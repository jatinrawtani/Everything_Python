num = int(input())
a=0
b=0
for i in range(1,(num*2)+1):
    if i%2==0:
        a=a+i
    else:
        b=b+i
print(b,a)