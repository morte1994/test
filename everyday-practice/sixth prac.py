__author__ = 'ss-pc'

inp = int(input("please input num >=3:  "))
a1 = 1
a2 = 1
a3 = 0
n = 0
print(a1)
print(a2)
if inp <= 2:
    print("you're wrong")
else:
    for n in range(3, inp + 1):
        a3 = a1 + a2
        print(a3)
        a1 = a2
        a2 = a3
print ("-"*100)
n = input()
x = 3
a1 = 1
a2 = 1
print a1
print a2
while x <= n:
    a3 = a1 + a2
    print a3
    a1 = a2
    a2 = a3
    x += 1
