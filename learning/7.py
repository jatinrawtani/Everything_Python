a=input("Enter the integer number")
n=float(a)
if (n%2==0):
    if (2<=n<=5 or n>20):
        print('not weird')
    elif (6<=n<=20):
        print('weird')
else:
    print('weird')