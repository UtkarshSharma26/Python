bu=6.9667
ba=4.0000
go=5.8340
jw=6.8334
ab=6.4667
gl=12.300
x=100
v=400
a,b,c,d,e,f=125,125,1,1,1,1
for a in range(x,200):
	print(a)
	for b in range(x,200):
		for c in range(x,200):
			for d in range(250,400):
				for e in range(200,400):
					for f in range(350,400):
						if(a+b+c+d+e+f==1184 and (round(bu*a)+round(ba*b)+round(go*c)+round(jw*d)+round(ab*e)+round(gl*f)==11563 or round(bu*a)+round(ba*b)+round(go*c)+round(jw*d)+round(ab*e)+round(gl*f)==11564)):
							#if(round(bu*a)+round(ba*b)+round(go*c)+round(jw*d)+round(ab*e)+round(gl*f)==11563 or round(bu*a)+round(ba*b)+round(go*c)+round(jw*d)+round(ab*e)+round(gl*f)==11564):
							print (a,b,c,d,e,f)
						#if((bu*a)+(ba*b)+(go*c)+(jw*d)+(ab*e)+(gl*f)>11565):






	
