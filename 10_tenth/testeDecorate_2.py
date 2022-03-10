#　装饰器
import time
def decorator(func):
    def wrapper(*args):
        print(time.time())
        func(*args)
    return wrapper

@decorator
def f1(fucn_name):
    print('This is a function name'+fucn_name)

@decorator
def f2(func_name1,func_name2):
    print('This is a function name'+func_name1)
    print('This is a function name'+func_name2)

f1('test_func')
f2('test_fucn1','test_func2')







