# encoding :utf-8

from lxml import etree
import urllib2

class Url():

    def __init__(self, url, header = None):
        self.__url = url
        self.__header = header

    def getHtml(self, header = None):
        header = {
            "Cookie": "nteslogger_exit_time=1543626455750; s_n_f_l_n3=70586b132499ffbc1543626453228; vinfo_n_f_l_n3=70586b132499ffbc.1.3.1543623073642.1543624252335.1543626453228; pgr_n_f_l_n3=70586b132499ffbc15436242249094015; ne_analysis_trace_id=1543624224900; _ntes_nnid=d7ffa7b1f9a5c9b9a07dcc065617d45f,1543623073630; _ntes_nuid=d7ffa7b1f9a5c9b9a07dcc065617d45f; JSESSIONID-WYBM=Xw9an8AVL%5C1OiMVpUuFrhqbt1XMfZ8sKNe3buqoziaw9JJwxNE8w11aBEes0gVacPeRSUazzV%2BPVnWFAx3ORNOMkJVUiL03Zt%2FGdBI5hQ18u%5C81CnyaPiHFZ%2Bk35%2FkV%2FaD%2Fhp7FYoCeL0JFjyFCnGBS7Ny7awfeUZc%2BD1IICFuyJlinp%3A1543716673403; _78x8309xiuyl_=31; JSESSIONID=abcwc7goZcWM7-RBTgNDw"
            ,"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0.3 Safari/604.5.6"}
        req = urllib2.Request(self.__url, headers = header)
        return urllib2.urlopen(req).read()

    def HtmlParse(self, html, parser):
        if html is None:
            return
        html = etree.HTML(html)
        hrefs = html.xpath(parser)
        if hrefs is None:
            return
        return hrefs