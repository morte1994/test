__author__ = 'ss-pc'

class Parent(object):
    def override(self):
        print("PARENT OVERRIDE()")
    def implicit(self):
        print("parent implicit")
    def altered(self):
        print("parent altered()")

class Child(Parent):
    def override(self):
        print("child override")
    def implicit(self):
        print("child implicit")
    def altered(self):
        print("child,before parent altered")
        super(Child,self).altered()
        print("child,after parent alter")

parent = Parent()
parent.override()
parent.implicit()
parent.altered()
print("-"*50)
child = Child()
child.override()
child.implicit()
child.altered()