from sys import argv

script, filename = argv

print"We're going to erase %r." % filename
print"If you don't want that,hit CTRL-C (^C)"
print"If you do want that, hit RETURN."

raw_input("?")

print "opening the file..."
target = open(filename,'w')         #����'w'�ļ�����д��(write)ģʽ������'r'��ʾ��ȡ�� read ��,'a'��ʾ׷��(append)

print "truncating the file.  Goodbye"
target.truncate()                   # ����ļ�

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
target.close                  # �ر��ļ����ļ� -> ����







