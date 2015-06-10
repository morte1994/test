__author__ = 'ss-pc'
import urllib2
request = urllib2.Request('http://www.baidu.com')
response = urllib2.urlopen(request)
print(response.geturl())    #geturl
print('-'*50)
print(response.info())  #info,dic describes condition from page
print('#'*200)
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

top_level_url = "http://example.com/foo/"

password_mgr.add_password(None, top_level_url, 'why', '1223')

handler = urllib2.HTTPBasicAuthHandler(password_mgr)

opener = urllib2.build_opener(handler)

a_url = 'http://www.baiduc.com'

opener.open(a_url)
urllib2.install_opener(opener)





