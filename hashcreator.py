import hashlib
def datatohash(data):
		return hashlib.md5(data).hexdigest()

		
"""		
x=raw_input("enter text")		
print datatohash(x)		
"""		
		
		
		
file_name = raw_input("enter file name ");
with open(file_name+".txt",'rb') as f:
	data = f.read()
	

	
hsh=datatohash(data)
with open(file_name+".hash",'w+') as f:
	f_write = f.write(hsh)
print hsh

