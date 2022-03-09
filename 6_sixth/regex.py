import re

a = 'C0C|C++|Java|Python|Javascript'

r = re.findall('Python', a)
if len(r) != 0:
    print('字符串中包含Python')
print(r)

# 找到字符串中的数字
print(re.findall('\d', a))

# Python 普通字符
# \d 元字符