people = raw_input("input people: ")
cars = raw_input('input cats: ')
buses = raw_input('input buses: ')

if cars > people:
  print "We should take the cars"
elif cars < people:
  print "we shouldn't take the cars"
else:
  print "we can't decide"

if buses > cars:
  print "That's too many buses."
elif buses < cars:
  print "Maybe we could take the buses."
else:
  print "We still can't decide."
if people > buses:
  print "Alright, let's just take the buses."
else:
  print "Fine, let's stay home then."


print "-----------------------------------------"
if cars > people and buses < cars:
  print "Oh,my godsh"
#���  elif  ���鶼��  True  ��  python  ����δ���Python  ֻ����������������  True  �ĵ�һ�����飬����ֻ�е�һ��Ϊ  True  ������ᱻ����
#
