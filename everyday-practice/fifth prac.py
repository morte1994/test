__author__ = 'ss-pc'
#输入一个值，输出以这个值为公比，1为首项的等比数列前10项

sun = 1
inp = input("please input num:  ")
for i in range(10):
    sun = inp ** i
    print(sun)



q = input()
n = 1
an = 1
while n <= 10:
    print an
    an *= q
    n += 1