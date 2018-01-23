states = {
	'Rajasthan' : 'RJ',
	'Madhya Pradesh' : 'MP',
	'Utter Pradesh' : 'UP',
	'Maharashtra' : 'MH',
	'Punjab' : 'PB'	
}

cities = {
	'RJ' : 'Jaipur',
	'MP' : 'Bhopal',
	'UP' : 'Kanpur'	
}

cities['MH'] = 'Mumbai'
cities['PB'] = 'Ludhiyana'

print '-' * 10
print "RJ state has:",cities['RJ']
print "MP state has:",cities['MP']

print '-' * 10
print "Rajasthan abbreviation is ", states['Rajasthan']
print "Punjab abbreviation is " , states['Punjab']

print '-' * 10
print "Rajasthan has :", cities[states['Rajasthan']]
print "Punjab has :" , cities[states['Punjab']]

print '-' * 10
for state , abbrev in states.items():
	print "%s has the city %s" %(state , abbrev)
	
print '-' * 10
for abbrev ,city in cities.items():
	print "%s has the city %s" %(abbrev , city)
	
print '-' * 10
for state , abbrev in states.items():
	print "%s state is abbreviated %s and has %s city " %(state, abbrev,cities[abbrev])

print '-' * 10
state = states.get('GA',None)

if not state:
	print "sorry No ,Goa"
	
city= cities.get('Goa' , 'Does not exist')
print "the city for state GA is %s " % city

# state.items return tuple = return two args name and type name is return to the state here and argument 