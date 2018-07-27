#Write a program to generate 10 random numbers between 1 to 100 such that there should one number between 1 to 10 one number between 11 to 20 etc.
import random
l = []

for i in range(10):
	if i == 0:
		l.append(random.randint(1,10))
	elif (i == 1):
		l.append(random.randint(11,20))
	elif i == 2:
		l.append(random.randint(21,30))
	elif i == 3:
		l.append(random.randint(31,40))
	elif i == 4:
		l.append(random.randint(41,50))
	elif i == 5:
		l.append(random.randint(51,60))
	elif i == 6:
		l.append(random.randint(61,70))
	elif i == 7:
		l.append(random.randint(71,80))
	elif i == 8:
		l.append(random.randint(81,90))
	elif i == 9:
		l.append(random.randint(91,100))
	else:
		pass
print(l)
