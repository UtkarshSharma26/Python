class calculator:
	
	def __init__(self , first , second):
		self.a=first
		self.b=second
		
		
	def add(self):
		return self.a + self.b
		
	def mul(self):
		return self.a * self.b
		
class scientific(calculator):
	
	def power(self):
		return self.a ** self.b
		
calc = calculator(10,20)

print "a+b: %d" %calc.add()
print "a*b: %d "%calc.mul()
scalc = scientific(2,3)
print "a+b: %d "%scalc.add()
print "a+b: %d "%scalc.mul()
print "a power b: %d" %scalc.power()