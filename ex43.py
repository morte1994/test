__author__ = 'ss-pc'
import ramdom
from urllib import urlopen
import sys

WORD_URL = ""
WORDS = []

PHRASES = {
    "class ###(###) :" : "make a class named $$$this is-a ###.",
    "class ###(object):\n\tdef __init__(self, ***)" : "class ### has-a __init__ that takes self and *** parameters.",
    "class ###(object):\n\tdef ***(self，@@@)" : "class ### has-a function named *** that takes self and @@@ parameters.",
    "*** = ###()" : "set *** to an instance of class ###",
    "***.***(@@@)" : "from *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'" : "From *** get the *** attribute and set it to '***'."
}

PHRASES_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] =="english":
    PHRASES_FIRST = True

for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in ramdom.sample(WORDS, snippet.count("###"))]
    other_names = ramdom.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_names.append(', '.join(random.sample(WORDS, param_count)))
    for sentence in snippet, phrase:
        results = sentence[:]

        for word in class_names:
            result = result.replace("###", word, 1)
        for word in other_names:
            result = result.replace("***", word, 1)
        for word in param_names:
            result = result.replace("@@@", word, 1)

