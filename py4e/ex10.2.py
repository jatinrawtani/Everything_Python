name = input("Enter file:")
handle = open(name)
dic=dict()
lst=list()
for line in handle:
    words = line.split()
    if line.startswith('From ') and len(words)>2 :
        h=line[5].split(':')
        lst.append(h[0])        
for i in lst:
    dic[i]=dic.get(i,0)+1
for k,v in sorted(dic.items()):
    print(k,v)