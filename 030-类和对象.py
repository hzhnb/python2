#继承
"""
__init__:相当于Java中的构造方法。如果想要把一个变量变成私有变量，那么只需要在__init__中把变量加上
__即可，如：self__name=name,想要在外部访问，使用get,set方法
"""
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
t = Student('Hugh',99)
print(t.get_name())

