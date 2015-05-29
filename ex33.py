i = raw_input()
m = raw_input()
number = []
if len(i) < len(m):    
  while len(i) < len(m):
    n = len(i)
    print "at the top i is %d" %n
    number.append(n)
    n = +1
    print "now,number is :", number
    print "at the buttom i is %d" %n
    
  print "at last,number is:",number


  for num in number:
    print num
else:
  print "repeat again"
