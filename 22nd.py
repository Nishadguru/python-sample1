#Python Program to Calculate the Number of Digits and Letters in a String

string= (input("Enter a word: "))
dig,alp = 0,0
for i in string:
	if i.isdigit():
		dig=dig+1
	elif i.isspace():
		pass
	else:
		alp=alp+1

print("The number of digits in the string is : ",dig)

print("The number of alphabets in the string are : ",alp)

