# 闭包 = 函数 + 环境变量(函数定义时候)
def curve_pre():
    a = 25 
    def curve(x):
        return a*x*x
    return curve
a = 10 
f = curve_pre()
print(f.__closure__)
print(f.__closure__[0].cell_contents)
print(f(2))

def f1():
    a = 10
    def f2():
        # a 在方法内部被赋值 会被python认为一个局部变量
        a = 20
        print(a)
    print(a)
    f2()
    print(a)
f1()

orgin = 0
def go(step):
    # 这一行 用非闭包的方式来解决闭包出现的问题
    global orgin
    new_pos = orgin + step
    orgin = new_pos
    return orgin

print(go(2))
print(go(3))
print(go(6))

def factory(pos):
    def go(step):
        # 这一行 用闭包的方式来解决闭包出现的问题
        nonlocal pos
        new_pos = pos +step 
        pos = new_pos
        return new_pos
    return go

tourist = factory(orgin)
print(tourist(2))
print(tourist(3))
print(tourist(5))
    
    