if __name__ == "__main__" :
    ## int
    print(type(1))
    print(type(-1))
    ## float
    print(type(1.1))
    print(type(1.1111))
    print(type(1+1.0))
    ## *
    print(type(1 *1.0))
    ## /
    print(type(1 / 1 ))
    print(type(1 // 1 ))
    ## 二进制 八进制 十六进制
    print(0b10);
    print(0o10);
    print(0x10);
    ## 进制转化
    print(bin(10));
    print(int(0b1010));
    print(hex(0b1010));
    ##bool布尔类型 真或假
    print(True);
    print(False);
    print(type(True));
    print(type(False));
    print(int(True));
    print(int(False));
    print(bool(1));
    print(bool(1.1));
    print(bool(0));
    print(bool('abc'));
    print(bool(''));
    print(bool([1,2,3]));
    print(bool([]));
    print(bool(None));

    # 字符串
    print('hello world')
    print("hello world")
    print(type('1'))
    print("let's go");
    print('let\'s go');
    print('''
     hello world
     hello world
     hello world
     ''');

    # 字符串运算
    print("hello"+"world")
    print("hello"*3)
    print("hello world"[0])
    print("hello world"[-1])
    print("hello world"[6])
    print("hello world"[-5])
    print("hello world"[0:5])
    print("hello world"[0:-1])
    print("hello world"[0:-3])
    print("hello world"[6:])
    print("hello world python java c# javascript php ruby"[0:-4])
    print("hello world python java c# javascript php ruby"[6:])
    print("hello world python java c# javascript php ruby"[:-4])

    ## 转义字符 r
    print('hello \n world')
    print('c:\northwind\northwest')
    print('c:\\northwind\\northwest')
    print(r'c:\northwind\northwest')
    print(R'c:\northwind\northwest')
    # print(r'let's go'); 错误写法

    # 列表
    print(type([1,2,3,4,5,6]))
    print(type(["hello,world",1,2,3,4,5,6]))
    print(type(["hello,world",1,2,3,4,5,6,True,False]))
    print(["hello,world",1,2,3,4,5,6,True,False][0])
    print(["hello,world",1,2,3,4,5,6,True,False][3])
    print(["hello,world",1,2,3,4,5,6,True,False][0:2])
    print(["hello,world",1,2,3,4,5,6,True,False][-1:])
    print(["hello,world",1,2,3,4,5,6,True,False]+ ["点燃","虚弱"])

    # 元组
    print((1,2,3,4,5))
    print((1,2,3,4,5)[0])
    print((1,2,3,4,5)[0:2])
    print((1,2,3,4,5)* 3)
    print(type((1,2,3,4,5)))
    print(type((1)))
    print(type((1,)))
    print(type(()))
    print(type([1]))

    # str list tuple 序列
    print("hello world"[2])
    print([1,2,3][2])
    # 切片
    print([1,2,3,4,5][0:3])
    print([1,2,3,4,5][-1:])
    print("hello world"[0:8:2])
    print(3 in [1,2,3,4,5,6])
    print(3 not in [1,2,3,4,5,6])
    print(len([1,2,3,4,5,6]))
    print(max([1,2,3,4,5,10]))
    print(min([1,2,3,4,5,10]))
    print(min([0,1,2,3,4,5,10]))
    print(min("abcde"))
    print(ord('w'))

    # Set 无序集合,没有重复元素
    print(type({1,1,2,2,3,4,5,6}))
    print(len({1,1,2,2,3,4,5,6}))
    print(1 in {1,1,2,2,3,4,5,6})
    print(1 not in {1,1,2,2,3,4,5,6})
    # 求两个集合的差集
    print({1,1,2,2,3,4,5,6} - {3,4})
    # 求两个集合的交集
    print({1, 1, 2, 2, 3, 4, 5, 6} & {3, 4})
    # 求两个集合的合集
    print({1, 1, 2, 2, 3, 4, 5, 6} | {3, 4,7})
    print(type({}))
    print(type(set()))
    # dict 字典
    # {key1:value1,key2:value2....}
    print(type({1:1,2:2,3:3}))
    print({"Q":"新月打击","W":"苍白之瀑","E":"月之降临","R":"月神冲刺"})
    print({"Q":"新月打击","W":"苍白之瀑","E":"月之降临","R":"月神冲刺"}["Q"])
    print({"Q":"新月打击","W":"苍白之瀑","E":"月之降临","R":"月神冲刺","Q":"test新月打击"}["Q"])
    print({"Q":"新月打击","W":"苍白之瀑","E":"月之降临","R":"月神冲刺","Q":"test新月打击",1:"新月打击"})
    # 变量  1、变量名首字符不能是数字  2、只能使用字母、数字、下划线  3、系统关键字不能用在变量名中 保留关键字  区分大小写
    A = [1,2,3,4,5,6]
    B = [1,2,3]
    skill = ['新月打击','苍白之瀑']
    print(A*3+B+skill)

    # int str tuple (不可改变)值类型  list set dict（可变） 引用类型
    # a =1 ;
    # b =a ;
    # a =3 ;
    # print(b)
    a  = [1,2,3,4,5]
    b = a
    a[0] = '1'
    print(a)
    print(b)
    print(hex(id(a)))
    a.append(4)
    print(a)
    e = (1,2,3,[4,5,6])
    print(e[3][1])

    # 算数运算符 - / // % **
    # 赋值运算符 = += *= /=  %= **= //=
    # 比较关系运算符 ==  != > <　＞＝　＜＝　  比较值是否相等
    #　逻辑运算符 and or not  int float 0被认为是false 非0表示true
    # 成员运算符 in not in  比较两个变量的值是否相等
    # 身份运算符 is  is not
    # 位运算符
    print(2**5)
    print([1,2,3 ] > [2,3,4])
    b= 1
    print(b in {"c":1})
    b = 'c'
    print(b in {"c":1})
    g = {1,2,3}
    h = {2,1,3}
    print(g==h)
    print(g is h)
    i = (1,2,3)
    j = (2,1,3)
    print(i == j)
    print(i in j)
    k = 'hello'
    print(type(k) == int)
    print(type(k) == str)
    print(isinstance(k,str))
    print(isinstance(k,(int,str,float)))
    # 对象的三个特征 id (is)  、 value（==）、type(isinstance)

    ### 位运算符  & 按位与 |按位或 ^ 按位异或 ～按位取反 <<左移动 >>右移动   都是对二进制数进行运算

    # 表达式是 运算符和操作数 所构成的序列

    # python 运算符 优先级  （http://c.biancheng.net/view/2190.html）

    # python 使用缩进来分隔代码和代码块 不像其他语言的()


