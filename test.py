def gold_room():
  print "this room is full of gold. how much do  you take?"
  next = raw_input("> ")
  
  if "0" in next or "1" in next:
    how_much = int(next)
    print "0 or 1"
  else:
    dead("man,learn to type a number")
  if how_much < 50:
    print "nice,you're not greedy, you win"
    exit(0)
  else:
    dead("ending")

def dead(why):
  print why, "zhong yu wan le"  
  exit(0)

gold_room()
