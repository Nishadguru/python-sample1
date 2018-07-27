#18. Python Program to Take in a String and Replace Every Blank Space with Hyphen.

name = str(input("Enter a word: "))
newname=''
for i in name:
	if i == ' ':
		newname = newname + '-'
	else:
		newname = newname + i
print(newname)
