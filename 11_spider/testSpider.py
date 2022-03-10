from urllib import request
# 找到最近具有唯一标识性的标签 作为定位标签
class Spider(object):
    url = 'https://www.huya.com/g/lol'

    def __fetch_content(self):
        r =request.urlopen(self.url)
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
        print(htmls)

    def go(self):
        self.__fetch_content()
        
spider = Spider()
spider.go()    
        