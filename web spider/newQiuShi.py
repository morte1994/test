__author__ = 'ss-pc'
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

class QSBK:
    def __init__(self):
        self.page = 1

        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []
        self.enablue = False
    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(page)
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            print(response.read())
            content = response.read().decode('utf-8')
            return pageIndex

        except  urllib2.URLError, e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            return None
            print("loading is wrong")
        pattern = re.compile(r'<div.*?class="author".*?>.*?\n<a.*?>\n<img.*?src="(.*?)".*?alt="(.*?)".*?/>\n</a>\n<a.*?>(.*?).*?</a>\n</div>\n+<div.*?class="content".*?>\n+(.*?)\n<!--(.*?)-->\n+</div>\n+[\s\S]*?<div.*?class="stats">\n<span.*?><i.*?>(.*?)</i>.*?</span>',re.S)
        items = re.findall(pattern, content)
        pageStories = []
        for item in items:
            haveImg = re.search("img", item[3])
            if not haveImg:
                pageStories.append([item[0].strip(), item[1].strip(), item[2].strip(), item[3].strip()])
        return  pageStories
    def loadPage(self):
        if self.enablue == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.getPageItems)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1
    def getOneStory(self, pageStories, page):
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input == "Q":
                self.enablue = False
                return
            print u"%dpage\tpeople:%s\ttime:%s\n%s\ngood:%s\n" %(page, story[0], story[1], story[2], story[3])
    def start(self):
        print(u"loading qsbk,watch new pages")
        self.enablue = True
        self.loadPage()
        nowPage = 0
        while self.enablue:
            if len(self.stories) > 0:
                pageStories = self.pageStories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories, nowPage)

opider = QSBK()
opider.start()