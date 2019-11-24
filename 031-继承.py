"""
继承：
class 子类名（父类名）:
注意：如果子类中定义与父类同名的方法或属性，则会自动覆盖父类的方法或属性
"""
class Parent:
    def hello(self):
        print('正在调用父类的方法')
class Child(Parent):
    pass
p = Parent()
p.hello()
c = Child()
c.hello()
class Child(Parent):
    def hello(self):
        print('正在调用子类的方法')
c1 = Child()
c1.hello()