try:
    num = int(input())
    l=list()
    for i in range(0,num):
        a=int(input())
        l.append(a)
    l.sort(reverse=True)
    for n in range(0,num):
        l[n]=l[n]*(n+1)
    print(max(l))
except:
    pass