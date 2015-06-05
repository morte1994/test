__author__ = 'ss-pc'

import urllib
yumain = 'http://www.liaoxuefeng.com'
path = r'F:\python'

input = open(r'F:\python','r')
head = input.read()

f = urllib.urlopen("http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000")
home = f.read()
f.close()

