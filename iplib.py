import urllib2
import json
data = urllib2.urlopen('http://api.ipify.org?format=json')
x=data.read()
print x
dict = json.loads(x)
print dict
print dict['ip']


#gives external ip address
#json used to store data 
#javascript object notation