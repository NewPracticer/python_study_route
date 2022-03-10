#　装饰器
print('装饰器1～～～～～～～～～～～～～～～～～')
import time
def f1():
    print('This is a function')

def print_current_time(func):
    print(time.time())
    func()

print_current_time(f1)
print('装饰器2～～～～～～～～～～～～～～～～～')
#　装饰器2
def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

f = decorator(f1)
f()
# 装饰器3
print('装饰器3～～～～～～～～～～～～～～～～～')
@decorator
def f2():
    print('This is a function')
f2()






