__author__ = 'ss-pc'
import urllib2
import cookielib
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print('name = '+ item.name)
    print('value = ' + item.value)

filename = 'cookie.txt'
cookie1 = cookielib.MozillaCookieJar(filename)
handler1 = urllib2.HTTPCookieProcessor(cookie1)
opener1 = urllib2.build_opener(handler1)
response1 = opener1.open("http://www.baidu.com")
cookie1.save(ignore_discard=True, ignore_expires = True)


cookie2 = cookielib.MozillaCookieJar()
cookie2.load('cookie.txt', ignore_discard=True, ignore_expires=True)



