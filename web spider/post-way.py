__author__ = 'ss-pc'
import urllib2
import urllib

values = {}
values['username'] = "1328087534@qq.com"
values['password'] = "blue1994"
data = urllib.urlencode(values)
url = "http://www.douban.com/accounts/login?redir=http://www.douban.com/doumail/"
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print(response.read())