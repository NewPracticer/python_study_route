# 类的基本作用：封装
# 类是现实世界或思维世界中的实体在计算机中的反映
# 它将数据以及这些数据上的操作封装在一起
# 类 - > 类变量
# 实例 - > 实例变量
class Student():

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



# 类的实例化
student = Student('xiao',18)
# student2 = Student('da',118)
Student.plus_sum()
student.print_file()
# student2.print_file()
# print(Student.name)
print(student.__dict__)

student2 = Student('zhong', 19)
Student.plus_sum()
student3 = Student('da', 20)
Student.plus_sum()
student3.marking(59)







        