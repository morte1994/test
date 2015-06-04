__author__ = 'ss-pc'
#coding:utf-8

import re
f = open("note-practice.txt")
readIng = f.read()
f.close()

useing = re.findall('[A-z]', readIng)
#readIng.sort()
readIng = '\t'.join(useing)


fnew = open("to.txt","w")
fnew.write(readIng)
fnew.close()

