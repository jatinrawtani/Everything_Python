import re
name = input("Enter file:")
handle = open(name)
sum=0

for line in handle:
	
	f = re.findall('[0-9]+',line)
	for num in f:
		if int(num) >= 1:
			sum = sum + int(num)
print(sum)