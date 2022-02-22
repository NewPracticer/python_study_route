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