num = int(input("Enter the number"))
rev = 0
while (num!=0):
	dig = num%10
	num = num/10
	rev = num + dig
print(rev)
