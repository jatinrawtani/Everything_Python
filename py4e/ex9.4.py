fname = input("Enter file name: ")
fh = open(fname)
lst=list()
dic=dict()
for line in fh:
    if line.startswith('From'):
        a=line.split()
        if len(a)>2:
            lst.append(a[1])
for word in lst:
    dic[word]=dic.get(word,0)+1
bigword=None
bigcount=None
for w,c in dic.items():
    if bigcount is None or c>bigcount:
        bigcount=c
        bigword=w
print(bigword,bigcount)