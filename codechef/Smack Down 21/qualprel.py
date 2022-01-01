t=int(input())
while t>0:
    t=t-1
    n,k=input().split()
    n,k=int(n),int(k)
    b=[]
    b=input().split()
    b.sort(reverse=True)
    score=b[k-1]
    count=0
    for j in b:
        if j>=score:
            count=count+1
    print(count)