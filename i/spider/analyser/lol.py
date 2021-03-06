import re

from analysis import Analyser

class LOL(Analyser):
    def __init__(self):
        # \s 获取所有字符 *匹配0次和无限多次 ?表示非贪婪模式  ()分组
        # self.parent_pattern = '<div class="video-info">([\s\S]*?)</div>'
        # self.name_pattern = '</i>([\s\S]*?)</span>'
        # self.number_pattern = '<span class="video-number">([\s\S]*?)</span>'
        self.parent_pattern = '<li class ="game-live-item" gid ="1">([\s\S]*?)</li>'
        self.name_pattern = '<i class ="nick" title ="([\s\S]*?)">[\s\S]*?</i>'
        self.number_pattern = '<i class = "js-num">([\s\S]*?)</i>'

    # 分析获取到的html文件
    def analysis(self, htmls):
        root_html = re.findall(self.parent_pattern, htmls)
        anchors = []
        for html in root_html:
            name = re.findall(self.name_pattern, html)
            number = re.findall(self.number_pattern, html)
            anchor = {'name':name, 'number':number}
            anchors.append(anchor)
        anchors = self.__refine(anchors)
        self.__sort(list(anchors))
    
    def __refine(self, anchors):
        g = lambda anchor : {
            'name': anchor['name'][0].strip(), 'number':anchor['number'][0]}
        return map(g, anchors)
    
    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        for rank in range(0, len(anchors)):
            print(
                ('rank ' + str(rank+1))
                + (': ' + anchors[rank]['name'])
                + '  ' + str(anchors[rank]['number']))
    
    def __sort_seed(self, anchor):
        r = re.findall('[\d\.]+', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number = number * 10000
        return number
            
            
        