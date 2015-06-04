__author__ = 'ss-pc'
import urllib2
import urllib
values = {}
values['username'] = ""
values['password'] = ""
data = urllib.urlencode(values)
url = "http://www.douban.com/accounts/login?redir=http://www.douban.com/doumail/"
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print(response.read())