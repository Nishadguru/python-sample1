#21. Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String.

name = str(input("Enter a name"))
B,S = 0,0
for i in name:
	if i.isupper():
		B=B+1
		
	if i.islower():
		S=S+1
		

print("The number of upper case letters : ", B)
print("The number of lower case ;etters : ", S) 
