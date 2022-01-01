N=int(input())
arr=[]
marksheet=[]
for i in range(N):
    name=input()
    marks=float(input())
    marksheet+=[marks]
    arr.append([name,marks])
x=sorted(set(marksheet))[1]
for n,s in sorted(arr):
    if s==x:
        print(n)