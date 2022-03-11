# 导入request包
from urllib import request
from factory import CategoryFactory
import analyser

class Spider():
    def __init__(self, url, analyser):
        self.url = url
        self.analyser = analyser
    
    # 从html页面获取数据
    def __fetch_content(self):
        with request.urlopen(self.url) as r:
            htmls = r.read()
            htmls = str(htmls, encoding = 'utf-8')
            return htmls
        
    def __analysis(self, htmls):
        # analyser= getattr(analyser, self.analyser) 
        # analyser = CategoryFactory.get_category(self.analyser)
        analyser.analysis(htmls)  
        
    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)
