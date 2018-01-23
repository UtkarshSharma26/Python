import hashlib
def datatohash(data):
		return hashlib.md5(data).hexdigest()

file_name = raw_input("enter file name");
with open(file_name+".txt",'rb') as f:
	data = f.read()
hsh=datatohash(data)
with open(file_name+".hash",'rb') as f:
	oldhsh = f.read()

if hsh == oldhsh:
	print "correct"
else:
	print "not correct"

 


