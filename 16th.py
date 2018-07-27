#16. Python Program to Replace all Occurrences of ‘a’ with $ in a String.

name = str(input("Enter a name : ")) 
newname = ''
for i in name:
	if i=='a':
		newname = newname + '$'
	else:
		newname = newname + i

print(newname)
