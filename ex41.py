__author__ = 'ss-pc'
class Thing(object):
#_init_ function rearch ,object, upper
    def __init__(self):
        self.number = 0
    def some_function(self):
        print("I got a call")
    def add_me_up(self, more):
        self.number += more
        return self.number

a = Thing()
b = Thing()
a.some_function()
b.some_function()
print("-"*50)
print(a.add_me_up(20))
print(b.add_me_up(30))
print("-"*50)
print(a.number)
print(b.number)
print("-"*50)
print(a.add_me_up(40))
print(a.number)

class Mult(object):
    def __init__(self, base):
        self.base = base
    def do_it(self, m):
        return m*self.base

print("-"*50)
x = Mult(a.number)
print(x.do_it(b.number))


