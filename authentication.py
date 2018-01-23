#usernamepassword
import hashlib


def datatohash(data):
		return hashlib.md5(data).hexdigest()

u_name=raw_input("Enter the User name : ")
u_pass=raw_input("Enter your password : ")

target = open("authentication.txt",'w')
x= target.write(u_pass)#--- write operation
target.close()

with open("authentication.txt",'rb') as f:
	data = f.read()
	
hsh=datatohash(data)
with open("authrntication.hash",'w+') as f:
	f_write = f.write(hsh)

		
		
with open("authentication.txt",'rb') as f:
	data = f.read()
hsh=datatohash(data)
with open("authrntication.hash",'rb') as f: 
	oldhsh = f.read()

if hsh == oldhsh:
	print "correct"
else:
	print "not correct"

