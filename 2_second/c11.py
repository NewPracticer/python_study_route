from third.c12 import *
a = 2
b = 3
d = 5 

## 模块的内置变量
# infos = dir()
# print(infos)

# c12为模块文件
# c11为入口文件
print('name:' + __name__)
print('doc:'+(__doc__ or '当前无注释'))
print('package:'+(__package__ or '当前没有任何包名'))
print('file:'+__file__)