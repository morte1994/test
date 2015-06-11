__author__ = 'ss-pc'
# -*- coding: utf-8 -*-


import urllib2
import urllib
import re
import time
import thread


class Spinder_model:

    def __init__(self):
        self.page = 1
        self.pages = []
        self.enablue = False

    def GetPage(self, page):
        myUrl = "http://m.qiushibaike.com/hot/page" +page
        user_agnt = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT'
        header = {'User-Agent': user_agnt}
        req = urllib2.Request(myUrl, header = header)
        myRes = urllib2.urlopen(req)
        myPage = myRes.read()

        unicodePage =myPage.decode("utf-8")

        myItems = re.findall('<div.*?id="content".?title="(.*?)">(.*?)</div>',
        unicodePage, re.S)
        items = []
        for item in myItems:
            item.append([item[0].replace("\n", ""),item[1].replace(("\n", ""))])
            return  item
    def LoadPage(self):
        while self.enablue:
            if len(self.pages) < 2:
                try:
                    myPage = self.GetPage(str(self.page))
                    self.page += 1
                    self.pages.append(myPage)
                except:
                    print("can't cennction on baike")
            else:
                time.sleep(1)
    def ShowPage(self,nowPage, page):
        for items in nowPage:
            print(u'NO.%d Page') %(page)
            print(items[0], items[1])
            myInput = 4#raw_input()
            if myInput == "quit":
                self.enablue = False
                break
    def Start(self):
        self.enablue = True
        page = self.page
        print(u'please waiting ,loading')

        thread.start_new_thread(self.LoadPage, ())

        while self.enablue:
            if self.pages:
                nowPage = self.pages[0]
                del self.pages[0]
                self.ShowPage(nowPage,page)
                page += 1

print u""