def add(b,c):
	return b+c

def sub(b,c):
	if b>c:		
		return b-c
	else:
		return c-b

def mul(b,c):
	return b*c

def div(b,c):
	return float(b)/c

def rem(b,c):
	return b/c

b= input("Enter 1st number ")
c= input("Enter 2nd number ")
a= raw_input("Enter the operator ")

if a=="+":
	x=add(b,c)
elif a=="-":
	x=sub(b,c)
elif a=="*":
	x=mul(b,c)
elif a=="/":
	x=div(b,c)
elif a=="%":
	x=rem(b,c)

print x