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
#4、post和get数据传送，请求和传输效果：get和post区别是get把数据显示放在URI中，并且对长度和数据编码有所限制，post请求把表单数据放在HTTP请求体中，且没有限制浏览器身份user-agent，包含头数据的字典
#5、header设置:
    # 识别服务器、反盗链的方式referer
    #User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求
    #Content-Type : 在使用 REST 接口时，服务器会检查该值，用来确定 HTTP Body 中的内容该怎样解析。
    #application/xml ： 在 XML RPC，如 RESTful/SOAP 调用时使用
    #application/json ： 在 JSON RPC 调用时使用
    #application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用在使用服务器提供的 RESTful 或 SOAP 服务时， Content-Type 设置错误会导致服务器拒绝服务
#6、代理proxy设置：
    #urllib2 默认会使用环境变量 http_proxy 来设置 HTTP Proxy。
#7、timeout设置：
#response = urllib2.urlopen('',data  ,timeout=10)
#8、http的put和delete方法:
#request = urllib2.Request(uri, data=data)
#request.get_method = lambda: 'PUT' # or 'DELETE'
#response = urllib2.urlopen(request)
#9、URLError:
#网络无连接，连接不到特定服务器，服务器不存在
#10、HTTPError：
#加入 hasattr属性提前对属性进行判断
#HTTPError实例产生后会有一个整型'code'属性，是服务器发送的相关错误号
#11、cookie:
    #opener:urlopen特殊的opener
    # cookielib：存储cookie对象，捕获cookie后续连接请求时重新发送，模拟登陆界面
    #保存cookie到文件cookie = cookielib.CookieJar()
#12.error：
#每个http应答对象response包含数字状态码

#1.Openers：
当你获取一个URL你使用一个opener(一个urllib2.OpenerDirector的实例)。
正常情况下，我们使用默认opener：通过urlopen。
但你能够创建个性的openers。
2.Handles：
Openers使用处理器handlers，所有的“繁重”工作由handlers处理。
每个handlers知道如何通过特定协议打开URLs，或者如何处理URL打开时的各个方面。
例如HTTP重定向或者HTTP cookies。

如果你希望用特定处理器获取URLs你会想创建一个openers，例如获取一个能处理cookie的opener，或者获取一个不重定向的opener。

要创建一个 opener，可以实例化一个OpenerDirector，
然后调用.add_handler(some_handler_instance)。
同样，可以使用build_opener，这是一个更加方便的函数，用来创建opener对象，他只需要一次函数调用。
build_opener默认添加几个处理器，但提供快捷的方法来添加或更新默认处理器。
其他的处理器handlers你或许会希望处理代理，验证，和其他常用但有点特殊的情况。

install_opener 用来创建（全局）默认opener。这个表示调用urlopen将使用你安装的opener。
Opener对象有一个open方法。
该方法可以像urlopen函数那样直接用来获取urls：通常不必调用install_opener，除了为了方便。
默认的openers有正常状况的handlers：ProxyHandler，UnknownHandler，HTTPHandler，HTTPDefaultErrorHandler， HTTPRedirectHandler，FTPHandler， FileHandler， HTTPErrorProcessor。
代码中的top_level_url 实际上可以是完整URL(包含"http:"，以及主机名及可选的端口号)。