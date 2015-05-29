states = {'oregon': 'or', 'florida': 'fl', 'california': 'ny', 'new york': 'ny', 'michigan': 'mi'}
cities = {'ca': 'san francisco', 'ny': "new york", 'or': 'portland'}

cities['nr'] = 'new york'
cities['or'] = 'portland'

print "ny state has: ", cities['ny']
print "or state has: ", cities['or']

print '-' * 10
print "Michigan's abbreviation is: ", states['michigan']
print "Florida's abbreviation is: ", states['florida']

print '-' * 10
print "Michigan has: ", cities[states['michigan']]
print "Florida has: ", cities[states['florida']]

print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

