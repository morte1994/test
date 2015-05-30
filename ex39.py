things = [1, 2, 3, 4]
print things[1], things
stuff = {'name': 'zed', 'age': 36, 'height': 6*12+2}
print stuff['name'] , stuff['age'], stuff['height']
stuff['city'] = "san francisco"
print stuff['city']
stuff[1] = "wow"
stuff[2] = "neato"
print stuff[1], stuff[2]


#rearch
#if we want to delete dir,so please use del this word
#find out all about dic,and dic which can't do
#items run
#collection.ordereadict


class Song(object):
    def sing_me(self):
        for line in self.lyrics:
            print(line)

    def __init__(self, lyrics):
        self.lyrics = lyrics

happy_birthday = Song(["happy", "birthday to you", "once more"])
bulls_on_parade = Song(["They rally around the family","With pockets full of shells"])
happy_birthday.sing_me()
bulls_on_parade.sing_me()



