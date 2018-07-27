# 15. Python Program to return true if all characters in the string are alphabetic and there is at least one other character, False.

name = str(input("Enter a name : "))
if name.isalpha():
	print("True  : It only contains alphabets ")
else:
	print("False : It contains specail characters")
