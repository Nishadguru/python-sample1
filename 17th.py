#17. Python Program to Count the Number of Vowels in a String.

word = str(input("Enter a word: "))
vowels = ['a','e','i','o','u']
vow = 0
for i in word:
	if i in vowels:
		vow=vow+1

print("The number of vowels in the entered string is :",vow)
