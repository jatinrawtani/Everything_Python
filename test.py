n = int(input())
a=list()
lst = input().split()
for i in lst:
    a.append(i)
ma = max(a)
print(ma)
c= a.count(ma)
for j in range(c):
    a.remove(ma)
#print(max(a))