# type -> int - >1
# type -> class ->obj

# object 是最顶层基类
# type也是一个类，同时也是一个对象
a =1 
b = 'abc'
print(type(1))
print(type(int))
print(type(b))
print(type(str))

class Student:
    pass
class MyStudent(Student):
    pass
stu = Student()
print(type(stu))
print(type(Student))
print(int.__base__)
print(str.__base__)
print(Student.__base__)
print(MyStudent.__base__)
print(type.__bases__)
print(type(object))
print(object.__base__)
