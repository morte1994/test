__author__ = 'ss-pc'
#proxy
import urllib2
proxy = True
handle = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
null_handle = urllib2.ProxyHandler({})
if proxy:
    opener = urllib2.build_opener(handle)
else:
    opener = urllib2.build_opener(null_handle)
urllib2.install_opener(opener)
print('*'*100)
print(opener)

#Timeout
import socket
import urllib2
socket.setdefaulttimeout(10)
urllib2.socket.setdefaulttimeout(20)

#header
#redirect
class RedirctHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        print "301"
        pass
    def http_error_302(self, req, fp, code, msg, headers):
        print("303")
        pass
opener = urllib2.build_opener(RedirctHandler)
#opener.open('http://rrurl.cn/b1UZuP')

#cookie
import urllib2
import cookielib
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response1 = opener.open('http://www.baidu.com')
print("*"*100)
for item in cookie:
    print(item.name)
    print(item.value)

#http put and delete
#e.code
#debug log

httpHandle = urllib2.HTTPHandler(debuglevel=1)
httpsHandle = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandle, httpsHandle)
urllib2.install_opener(opener)
response3 = urllib2.urlopen('http://www.baidu,com')

#list handle
import urllib
import urllib2
postdata = urllib.urlencode({})
req = urllib2.Request(url = '', data=postdata)
result = urllib2.urlopen(req)
print(result.read())
#brower:user-agent

#anti-leech
#
# #






























