import urllib2

req = urllib2.Request('http://www.baidu.com')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    if hasattr(e, "code"):
        print e.code    #hasattr judge the values
    if hasattr(e, "reason"):
        print e.reason
else:
    print("ok")