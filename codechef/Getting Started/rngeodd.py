a,b=input().split()
jatin = list(range(int(a),int(b)+1))
for num in jatin:
    if num%2==0:
        jatin.remove(num)
print(*jatin,sep=" ")