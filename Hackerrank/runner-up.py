n=int(input())
arr=list(map(int,input().split()))
b=set(arr)
b.remove(max(b))
print(max(b))