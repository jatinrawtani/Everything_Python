fname = input("Enter file name: ")
fh = open(fname)
lst=list()
for line in fh:
    if line.startswith('From'):
        a=line.split()
        if len(a)>2:
            lst.append(a[1])
count=0
for i in lst:
    count=count+1
    print(i)
print("There were", count, "lines in the file with From as the first word")
