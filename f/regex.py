import re

a = 'C0C|C++|Java|Python|Javascript'

r = re.findall('Python', a)
if len(r) != 0:
    print('字符串中包含Python')
print(r)

# 普通字符集
# 找出中间字母为c或者f的
s = 'abc,acc,adc,aec,afc,ahc'
r = re.findall('a[cf]c', s)
print(r)
# 找出中间字母不是c或者f的
s = 'abc,acc,adc,aec,afc,ahc'
r = re.findall('a[^cf]c', s)
print(r)
# 找出中间字母从c到f的
s = 'abc,acc,adc,aec,afc,ahc'
r = re.findall('a[c-f]c', s)
print(r)

### 概括字符集
# 找到字符串中的数字
print(re.findall('\d', a))
print(re.findall('[0-9]', a))
# 找到字符串中的非数字
print(re.findall('\D', a))
print(re.findall('^[0-9]', a))
# 匹配单词字符
print(re.findall('\w', 'python1111java&678php'))
print(re.findall('A-Za-z0-9_', 'python1111java&678php'))
# 匹配非单词字符
print(re.findall('\W', 'python1111java&678php\n\r\t'))
# 匹配空白字符
print(re.findall('\s', 'python1111java&678php\n\r\t'))
# . 匹配除换行符\n之外的任何字符

### 数量词
print(re.findall('[a-z][a-z][a-z]', 'python 11111java678php'))
print(re.findall('[a-z]{3}', 'python 11111java678php'))
print(re.findall('[a-z]{3,6}', 'python 11111java678php'))

### 非贪婪搜索
print(re.findall('[a-z]{3,6}?', 'python 11111java678php'))

### * 匹配0次或者无限多次
### + 匹配1次或者无限多次
### - 匹配0次或者1次
print(re.findall('python*', 'pytho1python1pythonn2'))
print(re.findall('python+', 'pytho1python1pythonn2'))
print(re.findall('python?', 'pytho1python1pythonn2'))
print(re.findall('python{1,2}', 'pytho1python1pythonn2'))
print(re.findall('python{1,2}?', 'pytho1python1pythonn2'))

### 边界匹配
print(re.findall('^\d{4,8}$', '1000000001'))
print(re.findall('^000', '1000000001'))
print(re.findall('000$', '1000000001'))

### 组 且的关系
print(re.findall('(Python){3}', 'PythonPythonPython')) 

### 匹配模式
print(re.findall('c#', 'PythonC#JavaPHP',re.I|re.S))
print(re.findall('c#.{1}', 'PythonC#\nJavaPH',re.I|re.S))

### 正则替换
print(re.sub('C#', 'go', 'PythonC#JavaPHP',0))
lanuage = 'PythonC#JavaC#PHPC#'
def convert(args):
    print(args)
    pass
print(re.sub('C#', convert, lanuage))

s = 'ABC324323EFD8384KDKD'
def convert2(args):
    matched = args.group()
    if int(matched)>=6:
        return '9'
    else:
        return '0'
print(re.sub('\d', convert2, s))

### match 和search 
s = 'ASDF234LKJASDF234DS87234'
# 匹配第一个字母并返回结果
print(re.match('\d', s))
# 找到第一个符合要求的结果，并返回 
print(re.search('\d', s))

### group分组
s = 'life is short, i use python,i love python'
r = re.findall('life(.*)python(.*)python', s)
print(r)


