__author__ = 'ss-pc'
import string, urllib2

def tieba(url, begin_page, end_page):
    for i in range(begin_page, end_page):
        sName = string.zfill(i, 5)+'.html'
        print('loading the' + str(i) + 'page and save it named' + sName + '...')


        f = open(sName, 'w')
        m = urllib2.urlopen(url + str(i)).read()
        f.write(m)
        f.close()

url = 'http://www.baidu.com'
begin_page = 1
end_page = 9
tieba(url, begin_page, end_page)
