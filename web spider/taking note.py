__author__ = 'ss-pc'

#1、URL的格式由三部分组成：
#①第一部分是协议(或称为服务方式)。
#②第二部分是存有该资源的主机IP地址(有时也包括端口号)。
#③第三部分是主机资源的具体地址，如目录和文件名等。

#2、urlopen(url, data, timeout)
#第一个参数url即为URL，第二个参数data是访问URL时要传送的数据，第三个timeout是设置超时时间。
#第二三个参数是可以不传送的，data默认为空None，timeout默认为 socket._GLOBAL_DEFAULT_TIMEOUT
#第一个参数URL是必须要传送的，执行urlopen方法之后，返回一个response对象，返回信息便保存在这里面。


#3、构造request，多写一个request对象，在构建请求时还需要加入内容，通过构建request，服务器响应请求得到应答
#4、post和get数据传送