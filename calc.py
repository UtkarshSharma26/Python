"""calculator program a==+, b,c,
perform the operation on b,c
take user input
"""
b= input("Enter 1st number ")
c= input("Enter 2nd number ")
a= raw_input("Enter the operator ")
d=1
if a=="+":
	d=b+c
	print "Sum is ",d
elif a=="-":
	if b>c:
		d=b-c
		print "Difference is",d
	else:
		d=c-b
		print "Difference is",d
elif a=="*":
	d=b*c
	print "Product is ",d
elif a=="/":
	d=float(b)/c
	print "Quotient is ",d
elif a=="%":
	d=b%c
	print "Remainder is ",d
else:
	print "Invalid operator "

	