def break_words(stuff): 
  """This function will break up word for us"""
  words = stuff.split(' ')
  return words
def sort_words(words):
  """sorts the words"""
  return sorted(words)
def print_first_word(words):
  """Prints the first word after popping if off."""
  word = words.pop(0)
  return word
def print_last_word(words):
  """prints the last word after popping it off"""
  word = words.pop(-1)
  return word

def sort_sentense(sentense):
  """takes in a fill sentense and return the sorted words"""
  words = break_words(sentense)
  return sort_words(words)
def print_first_and_last(sentense):
  """print the first and last words ofthe sentense"""
  words = break_words(sentense)
  print_first_word(words)
  print_last_word(words)
def print_first_and_last_sorted(sentense):
  """sorts the words then prints the first and last sentense"""
  words = sort_sentense(sentense)
  print_first_word(words)
  print_last_word(words)

#x = raw_input('please input')
#y = sort_sentense(x)
#print y
#input variable ,so all the function bianli all

