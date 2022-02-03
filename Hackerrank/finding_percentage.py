N=int(input())
db={}
for i in range(N):
    name,a,b,c=input().split()
    a,b,c=float(a),float(b),float(c)    
    db[name]=[a,b,c]
x=input()
if x in db:
    j=(sum(db[x])/3)
    print("%.2f"%j)