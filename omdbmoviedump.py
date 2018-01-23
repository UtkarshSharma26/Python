import json
import urllib2
txtfile1=open('out.txt','r')
target=txtfile1.read()
print target

dict = json.loads(target)
print dict

for x,y in dict.items():
	print x,y
	
#print dict['ip']


txtfile1.close()