handle=open('text.txt')
count= 0
for lines in handle:
    count=count+1
print("There are",count,"number of lines in the text.txt file.")

while True:
    fn=input("If you want to see all the matter in the file, then enter 'show' otherwise enter 'exit'.\n")
    if fn=="show":
        handle=open('text.txt')
        for l in handle:
            l=l.rstrip()
            print(l.upper())
    if fn=="exit":
        print('The program has now ended.')
        exit()
    else:
        print('Invalid input')
        continue
