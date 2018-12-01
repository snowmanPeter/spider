# encoding:utf-8

from com.zkk.Util.Url import Url

URL = "http://caipiao.163.com/award/11xuan5/{}.html"


class Lottery_11To5():

    def __init__(self, start, end, flag, url):
        __start = start
        __end = end
        __flag = flag
        __url = url

    def setStart(self, start):
        self.__start = start

    def getStart(self):
        return self.__start

    def setEnd(self, end):
        self.__end = end

    def getEnd(self):
        return self.__end

def main():
    url = Url(URL.format("20171212"))
    html = url.getHtml()
    print html
    hrefs = url.HtmlParse(html, parser=u'//td[@class="start"]')
    print hrefs

if __name__ == '__main__':
    main()