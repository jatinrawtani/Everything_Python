largest=-1
smallest=None
while True:
    num=input("Enter a number: ")
    if num=="done":
        break
    try:
        n=int(num)
        if n>largest:
            largest=n
        if smallest==None:
            smallest=n
        elif n<smallest:
            smallest=n
        continue
        
    except:
        print("Invalid input")
        continue    

print("Maximum is",largest)
print("Minimum is",smallest)