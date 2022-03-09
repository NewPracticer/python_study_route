from c16 import Human

# 可以多继承
class Student(Human):
    
    # name = 'skyl'
    # age = 0
    # sum = 0
    # score = 0 
    # # 私有成员变量
    # __scr = 0
    # # 实例方法
    # def __init__(self,name,age):
    #     # 构造函数
    #     # 初始化对象的属性
    #     self.name = name
    #     self.age = age
    #     # print(age)
    #     # print(name)
    #     self.__class__.sum +=1
    #     print('当前班级学生总数为：'+str(self.__class__.sum))

    def __init__(self,school,name,age):
        self.school = school
        # 调用父类构造函数
        # Human.__init__(self,name, age)
        super(Student,self).__init__(name, age)

    def do_homework(self):
        super(Student, self).do_homework()
        print('english homework')



student1 = Student('上海小学','不敢当',18)
# print(student1.sum)
print(student1.name)
print(student1.age)
# print(Student.sum)
print(student1.do_homework())