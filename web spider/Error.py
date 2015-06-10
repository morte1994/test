__author__ = 'ss-pc'
import urllib2
req = urllib2.Request('http://bbs.csdn.net/callmewhy')
try:
    urllib2.urlopen(req)
except urllib2.URLError, e:
    if hasattr(e, 'code'):
        print(e.code)
    elif hasattr(e, 'reason'):
        print(e.reason)
    else:
        print('everything is fine')