n= input("Enter the number")

pal=0
temp = n
while (n>0):
	dig= n%10
	pal= 10*pal+ dig
	n=n/10
print(pal)
if (temp==pal):
	print("The number is a palindrome")
else:
	print("The number is not a palindrome")


