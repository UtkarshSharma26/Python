print("""
1- factorial
2- prime
3- prime in a range
4- fibonaci
5- reverse
6- armstrong number"""	)

a= input("Enter the choice ")

if a==1:
	n=input("Enter the number ")
	fact=1
	while n>=1:
		fact=fact*n
		n=n-1
	print "The factorial is",fact	

if a==2:
	c=1
	b=input("Enter a number ")
	for n in range(2,(b/2)+1):
		if b%n==0:
			c=0
			break
		else:
			c=1
	if c==0:
		print("Not Prime number ")
	else: 
		print("Prime number ")

if a==3:
	b=input("First Number ")
	c=input("Last Number ")
	for n in range(b,c):
		d=1
		for m in range(2,(n/2)+1):
			if n%m==0:
				d=0
				break
			else:
				d=1		
		if d==1:
			print n

if a==4:
	n=input("Number of terms ")
	b=0
	c=1
	d=0
	print b 
	print c
	for i in range(0,n):
		d=b+c
		b=c
		c=d
		i=i+1
		print d

if a==5:
	n=input("Enter the number ")
	rev=0
	while n>0:
		r=n%10
		rev=(rev*10)+r
		n=n/10
	print "The reverse is print ",rev

if a==6:
	num=input("Enter the number to be checked ")
	sum=0
	t=num
	while t>0:
		rem=t%10
		sum=sum+(rem**3)	
		t=t/10
	if num==sum:
		print (num,"is a armstrong number")
	else:
		print (num,"is not a armstrong number")




	
		


		




