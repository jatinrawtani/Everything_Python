try:
    num=int(input())
    if (num%5==0 and num%11!=0) or (num%11==0 and num%5!=0):
        print('ONE')
    elif num%5==0 and num%11==0:
        print('BOTH')
    else:
        print('NONE')
except:
    pass