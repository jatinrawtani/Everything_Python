num = int(input())
jatin = list()
for i in range(1,num+1):
    if (num%i==0):
        jatin.append(i)
print(len(jatin))
print(*jatin,sep=" ")