__author__ = 'ss-pc'
#urlopen(url, data, timeout)
#第一个参数url即为URL，第二个参数data是访问URL时要传送的数据，第三个timeout是设置超时时间。
#第二三个参数是可以不传送的，data默认为空None，timeout默认为 socket._GLOBAL_DEFAULT_TIMEOUT
#第一个参数URL是必须要传送的，执行urlopen方法之后，返回一个response对象，返回信息便保存在这里面。
import urllib2
def pri(x):
    f = open("to.txt", "w")
    f.write(x)
    f.close()
#response = urllib2.urlopen("http://www.douban.com")

request = urllib2.Request("http://www.douban.com")
response = urllib2.urlopen(request)
pri(response.read())

