__author__ = 'ss-pc'

import urllib
import urllib2

url = "http://www.server.com/login"
user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"

values = {'username':'','password':''}
headers = {'User-Agent': user_agent}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
response = urllib2.urlopen(request)
print(response.read())

import urllib2
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)