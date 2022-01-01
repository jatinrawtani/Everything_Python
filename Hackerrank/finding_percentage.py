N=int(input())
db={}
for i in range(N):
    name,db[name]=input(),float(input().split())
x=input()
if x in db:
    print(sum(db[x])/3)