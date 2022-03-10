# lambda 表达式
# lambda parmater_list ：expression

# 匿名函数
def add(x,y):
    return x+y
print(add(1, 2))
f = lambda x,y : x+y
print(f(1,2))


# 三元表达式
# x if x >y else y

# map
list_x = [1,2,3,4,5,6,7,8]
list_y = [1,2,3,4,5,6,7,8]
def square(x):
    return x*x
# for x in list_x:
#     square(x)
r = map(square, list_x)
print(list(r))
r = map(lambda x,y:x*x+y, list_x,list_y)
print(list(r))

# reduce 连续的计算
from functools import reduce
#((((1+2)+3)+4)+5)
r = reduce(lambda x,y:x+y, list_x)
print(r)
list_zimu = ['1','2','3','4','5','6','7','8']
# a 为初始值
r = reduce(lambda x,y:x+y, list_zimu,'a')
print(r)

# filter
list_x = [1,0,1,0,1,0]
r = filter(lambda x:True if x==1 else False, list_x)
print(list(r))