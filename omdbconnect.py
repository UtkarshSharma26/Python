import json
import urllib2


url="http://www.omdbapi.com/?i=tt3896198&apikey=8da1ec4f"


#this takes a json string and loads it to a object which is a python object 
#represent of that string 
#omdb=open movie database
data =json.load(urllib2.urlopen(url))

for x,y in data.items():
	print x,y