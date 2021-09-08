num = int(input())
count=0
for i in range(1,num+1):
    for j in range(1,6):
        count=count+1
        if (i%2!=0):
            print(count,end=" ")
        if (i%2==0):
            if j==1:
                print(count+4,end=" ")
            if j==2:
                print(count+2,end=" ")
            if j==3:
                print(count,end=" ")
            if j==4:
                print(count-2,end=" ")
            if j==5:
                print(count-4,end=" ")
    print()