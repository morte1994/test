 # -*- coding: utf-8 -*- 
print """You enter a dark room ith doors.
Do you go throngh door #1 or door #2?
"""
door =  raw_input('> ')
if door == "1":
  print "There's a giant bear here eating a cheese cake. What do you do?"
  print "1.take the cake"
  print "2. Scream at the bear"

  bear = raw_input('> ')

  if bear == "1":
    print "The bear eats your face off. Good job!"
  elif bear == "2":
    print "The bear eats your legs off. Good job!"
  else:
    print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
  print "You stare into the endless abyss at Cthulhu's retina."
  print "1. Blueberries."
  print "2. Yellow jacket clothespins."
  print "3. Understanding revolvers yelling melodies."

  insanity = raw_input('> ')

  if insanity == "1" or insanity == "2":
    print "Your body survives powered by a mind of jello. Good job!"
  else:
    print "The insanity rots your eyes into a pool of muck. Good job!"

else:
  print "You stumble around and fall on a knife and die. Good job!"


#怎样判断一个数字处于某个值域中？两个办法：经典语法是使用  1 < x < 10 ，或者用  x in range(1, 10)  也可以
    
