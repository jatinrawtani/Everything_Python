handle=open('text.txt')
for lines in handle:
    line=lines.rstrip()
    print(line.upper())