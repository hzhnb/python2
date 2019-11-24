#魔法方法是被双下划线包围
#__init__(self,...]:类在实例化对象首先会调用的一个方法
class Rectangle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def gerPeri(self):
        return (self.x+self.y)*2
    def getArea(self):
        return self.x*self.y
rect = Rectangle(3,4)
print(rect.gerPeri())
#__new__(cls[..]):在类实例化是首先调用的方法
#class CapStr(str):
 #   def __new__(cls, *args, **kwargs):
#__del__(self):在所有的代码都执行完之后就会自动调用，回收对象，如果使用del 对象则会提前回收对象
class C:
    def __init__(self):
        print('我是init方法，我被调用了')
    def aa(self):
        print('我真的很无语！')
    def __del__(self):
        print('我是del方法，我被调用了')
c = C()
#del c
print('哈哈哈哈哈')