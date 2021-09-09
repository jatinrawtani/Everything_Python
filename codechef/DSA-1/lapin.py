a=int(input())
for b in range(0,a):
    word=input()
    #even
    if len(word)%2==0:
        l=word[:len(word)//2]
        r=word[len(word)//2:]
        for i in l:
            if i not in r :
                print("NO")
                break
            elif (l.count(i)!=r.count(i)) :
                print("NO")
                break
        else:
            print("YES")
        
    #odd
    if len(word)%2!=0:
        l=word[:(len(word)-1)//2]
        r=word[((len(word)-1)//2 +1):]
        for i in l:
            if i not in r :
                print("NO")
                break
            elif  (l.count(i)!=r.count(i)):
                print("NO")
                break
        else:
            print("YES")