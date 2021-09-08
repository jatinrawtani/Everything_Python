a=None
b=0
while True:
    n=input('Enter the number : ')
    if n=='done':
        break
    try:
        num=int(n)
        b=b+1
        if a==None:
            a=num
        elif a!=None:
            a=a+num
        continue
    except:
        print('Invalid input dost')
print('Sum of all numbers :',a)
print('count of all numbers :',b)
print('Average of all numbers =',a/b)