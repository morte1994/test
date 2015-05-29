#≤È‘ƒrange”√∑®
#hairs = ['brown', 'blond', 'red']
#eyes = ['brown', 'blue', 'green']
#weights = [1, 2, 3, 4]

#print [num for num in weights]
the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'orange', 'pear' ,'apricot']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for num in the_count:
  print "this is count %d" % num
for fruit in fruits:
  print "a fruit of type: %s" % fruit
for i in change:
  print "I got %r" % i

ele = []

for i in range(0, 6):
  ele.append(i)
  print "adding %d to the list" %i

for i in ele:
  print "ele was: %d" % i
