stud = {}

while True:
	sub = raw_input("Enter the subject ")
	if sub == 'End' or sub== 'end' or sub == 'END':
		break
	else:
		marks = input("Enter the marks ")
		stud[sub]=marks
		print ("\n")

print stud

count = 0
sum = 0
for x in stud.values():
	sum = sum + x
	count = count + 1

avg = sum/count
print avg 

