from sys import argv

script, filename = argv

print"We're going to erase %r." % filename
print"If you don't want that,hit CTRL-C (^C)"
print"If you do want that, hit RETURN."

raw_input("?")

print "opening the file..."
target = open(filename,'w')         #用了'w'文件就是写入(write)模式。还有'r'表示读取（ read ）,'a'表示追加(append)

print "truncating the file.  Goodbye"
target.truncate()                   # 清空文件

print "now I'm going to ask you for three lines"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "and finally, we close it"
target.close                  # 关闭文件。文件 -> 保存








