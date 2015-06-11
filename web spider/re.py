__author__ = 'ss-pc'
import re
pattern = re.compile(r'hello')
result = re.match(pattern,'hasodlo')

if result:
    print(result.group())
else:
    print('there is something wrong')














