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
#4、post和get数据传送，请求和传输效果
#5、header设置:识别服务器、反盗链的方式
    #User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求
    #Content-Type : 在使用 REST 接口时，服务器会检查该值，用来确定 HTTP Body 中的内容该怎样解析。
    #application/xml ： 在 XML RPC，如 RESTful/SOAP 调用时使用
    #application/json ： 在 JSON RPC 调用时使用
    #application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用在使用服务器提供的 RESTful 或 SOAP 服务时， Content-Type 设置错误会导致服务器拒绝服务