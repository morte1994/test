__author__ = 'ss-pc'
#get获取信息，post传递信息
import urllib
import urllib2
values = {}
values['username'] = ""
values['password'] = ""
data = urllib.urlencode(values)
url = ""

geturl = url + "?" + data

request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print(response.read())










