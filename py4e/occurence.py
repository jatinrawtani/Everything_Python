handle=open('text.txt')
dict=dict()
for lines in handle:
    lines=lines.rstrip()
    words=lines.strip()
    dict[words]=dict.get(words,0)+1
lst=list()
for key,value in dict.items():
    tple=(value,key)
    lst.append(tple)
print(sorted(lst[:5],reverse=True))
# printing 5 most occured words in the text file.