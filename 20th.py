#20. Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions.

string  = str(input("Enter a Word: "))
string1 = str(input("Enter a word: "))
count  = 0
count1 = 0
for i in string:
	count = count+1
print(count)

for j in string1:
	count1=count1+1
print(count1)

if (count>count1):
	print("The string with highest length is  ", count)

else:
	print("The string with lowest length is  ", count1)
		
