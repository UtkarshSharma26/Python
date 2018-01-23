import urllib,urllib2
#http://www.omdbapi.com/?t=go&y=plot=short&r=json
import json

url="http://www.omdbapi.com/?"

#title="white house down"
title=raw_input("enter the movie name")
year=""
length="short"
type="json"

values = {'t' : title}

data = urllib.urlencode(values)
print data 

req=url+data+"&apikey=8da1ec4f" 
print req
response=urllib2.urlopen(req)  #json format
dict=json.load(response)
jsondata = json.dumps(dict) #dictionary to json object
print jsondata

txtfile =open('out.txt','w')
txtfile.write(jsondata)
txtfile.close()