def add(a, b):
  print "adding %d + %d" % (a, b)
  return a + b

def subtract(a, b):
  print "subtracting %d - %d" % (a, b)
  return a - b

def multiply(a, b):
  print "multiply %d * %d" % (a, b)
  return a * b

def divide(a, b):
  print "divide %d * %d" % (a, b)
  return a / b

print "Let's do some math with just functions!"

age = add(2,4)
height = subtract(24, 42)
weight = multiply(21, 34)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ", what, "Can you do it by hand?"


#浏览器登陆 bitbucket.org ，搜索 “ python”
#• github.com • launchpad.net• koders.com
#  https://github.com/zedshaw/lamson
