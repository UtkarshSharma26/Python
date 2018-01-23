class calculator:
	def __init__(self , first ,second):
		self.a=first
		self.b=second
		
		
	def add(self):
		return self.a+self.b
		
	def mul(self):
		return self.a * self.b
		
	def sub(self):
		return self.a - self.b
		
	def divis(self):
		return float(self.a) / float(self.b) 

calc = calculator(10,20)

print "a+b: %d" %calc.add()
print "a * b :%d" % calc.mul() 
print "a - b :%d" % calc.sub() 
print "a / b :%f" % calc.divis() 