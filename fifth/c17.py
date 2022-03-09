import c16

class Student(c16.people):
    
    name = 'skyl'
    age = 0
    sum = 0
    score = 0 
    # 私有成员变量
    __scr = 0
    # 实例方法
    def __init__(self,name,age):
        # 构造函数
        # 初始化对象的属性
        self.name = name
        self.age = age
        # print(age)
        # print(name)
        self.__class__.sum +=1
        print('当前班级学生总数为：'+str(self.__class__.sum))

    def print_file(self):
        print('name: '+self.name)
        print('age:  '+str(self.age))

    #私有方法
    def __print_file_private(self):
        print('name: '+self.name)
        print('age:  '+str(self.age))

    #类方法
    @classmethod
    def plus_sum(cls):
        cls.sum +=1 
        print(cls.sum)

    @staticmethod
    def add(x,y):
        print('This is a static method')

    def marking(self,score):
        self.score = score;
        print(self.name)