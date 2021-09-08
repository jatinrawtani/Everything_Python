fname = input("Enter file name: ")
fh = open(fname)
lst = list()
new=[]
for line in fh:
    line.strip()
    lst.append(line.split())
for sublist in lst:
    for val in sublist:
        if val not in new:
            new.append(val)
print(sorted(new))