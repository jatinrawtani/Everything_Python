# Use the file name mbox-short.txt as the file name
count = 0
add=0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        line.replace(" ","")
        pos = line.find(':')
        a=float(line[pos+1:])
        add=add+a
average=add/count
print('Average spam confidence: ',average)