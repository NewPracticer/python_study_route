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
    ## 字符串
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
    ## 字符串运算
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
    ## print(r'let's go'); 错误写法
    ## 列表
    print(type([1,2,3,4,5,6]))
    print(type(["hello,world",1,2,3,4,5,6]))
    print(type(["hello,world",1,2,3,4,5,6,True,False]))
    print(["hello,world",1,2,3,4,5,6,True,False][0])
    print(["hello,world",1,2,3,4,5,6,True,False][3])
    print(["hello,world",1,2,3,4,5,6,True,False][0:2])
    print(["hello,world",1,2,3,4,5,6,True,False][-1:])
    print(["hello,world",1,2,3,4,5,6,True,False]+ ["点燃","虚弱"])
    ## 元组
    print((1,2,3,4,5))
    print((1,2,3,4,5)[0])
    print((1,2,3,4,5)[0:2])
    print((1,2,3,4,5)* 3)
    print(type((1,2,3,4,5)))
    print(type((1)))

