__author__ = 'ss-pc'
import urllib2
def pri(x):
    f = open("to.txt", "w")
    f.write(x)
    f.close()
#response = urllib2.urlopen("http://www.douban.com")

request = urllib2.Request("http://www.douban.com")
response = urllib2.urlopen(request)
pri(response.read())

