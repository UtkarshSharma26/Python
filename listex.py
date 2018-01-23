ten_things = "Apples Oranges Crows Telephone Light sugar"
print "wait there's not 10 things in that list , let's fix that . "

stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","boy"]

while len(stuff)!=10:
	next_one=more_stuff.pop()
	print "Additing",next_one
	stuff.append(next_one)
	#stuff.append(next_one)
	print "There's %d items now "%len(stuff)

print "There we go:",stuff
print "Lets do some things with stuff "
print stuff[1]
print stuff[-1]  #last element
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])
