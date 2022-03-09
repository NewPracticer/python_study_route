# 函数 (功能性，隐藏细节，避免编写重复代码)
## 参数列表可以没有 返回可以为空值 或者 return value 
import sys
##设置递归次数
sys.setrecursionlimit(100000)

def add(x,y):
    result = x+y;
    return result;

def printcode(args):
    print(args)

# 返回多个值
def damage(skill1,skill2):
    damage1 = skill1 *3
    damage2 = skill2 *2 +10
    return damage1,damage2

if __name__ == '__main__':
    result = add(3, 5)
    printcode(result);
    # 序列解包
    # 接受多个返回值
    skill1_damage,skill2_damage = damage(3, 6)
    print(skill1_damage , skill2_damage)

d=1,2,3
# a,b =d 
a,b,c =d
print(a)
print(b)
print(c)

## 函数的参数

### 1. 必须参数  
def addParameter(x,y):
    result = x+y;
    return result;

### 2. 关键字参数
c = addParameter(y=3, x=4)
print(c)

### 3. 默认参数
def print_student_files(name,gender='man',age=18,college='xiaoxue'):
    print('我叫：'+name)
    print('我今年：'+str(age) +'岁')
    print('我是' +gender)
    print('我在' + college +'上学')
print_student_files('小鸡', '男', 10, '人民路小学')
print('~~~~~~~~~~~~~~~~~~~')
print_student_files('小鸭')
print('~~~~~~~~~~~~~~~~~~~')
print_student_files('石敢当')
print('~~~~~~~~~~~~~~~~~~~')
print_student_files('喜小乐','女',16)
print('~~~~~~~~~~~~~~~~~~~')
print_student_files('果果',age=17)   

### 4.可变参数
def demo(*param):
    print(param)
    print(type(param))
demo(1,2,3,4,5,6)
a = (1,2,3,4,5,6,7)
demo(*a)

def demo3(param1,param2 =2 ,*param):
    print(param1)
    print(param2)
    print(param)

demo3('a',1,2,3,4)

### 5.关键字参数
def city_temp(**args):
    print(args)
    print(type(args))
    for key,value in args.items():
        print(key,':',value)

city_temp(xb = 'a',de ='b',ck='c')
a = {'bj':'32c','sh':'31c'}
city_temp(**a)

## 变量的作用域  
g = 10 #全局变量
def demo4():
    g =20 #局部变量
    print(g)
demo4()
### python没有块级作用域
def demo5(args):
    c = 0
    for i in range(0,9):
        a ='a'
        c +=1
    print(c)
    print(a)
demo5(1)    
### global 全局变量
def demo6(args):
    global z
    z =2 ; 

demo6(1)
print(z)


