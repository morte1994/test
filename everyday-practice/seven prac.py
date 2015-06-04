
n = input()
for i in range(1, n+1):
    for j in range(0, n-i):
        print '',
    for j in range(0, i):
        print('*'),
    print
print("&"*50)
for i in range(1, n+1):
    for j in range(0, n-i):
        print ' ',
    for j in range(0, i):
        print(' * '),
    print


