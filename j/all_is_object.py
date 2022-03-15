'''
    函数和类也是对象
    1、赋值给一个变量
    2、可以添加到集合中
    3、可以作为参数传递给函数
    4、可以当作函数的返回值
'''
def ask(name = 'skyl'):
    print(name)
my_func = ask
my_func('function skyl')

class Person(object):
    def __init__(self):
        print('class skyl')
my_class = Person 
my_class()

obj_list = []
obj_list.append(my_func)
obj_list.append(my_class)
for item in obj_list:
    print(item())

def decorator_func():
    print('dec start')
    return ask
my_dec_ask  =decorator_func()
my_dec_ask('tom')


        


    