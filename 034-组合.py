#组合：把类的实例化放到一个新类里面， 把几个没有直接关系的类放在一起
class Turtle:
    def __init__(self,x):
        self.num = x
    def aaa(self):
        print('哈哈哈')
class Fish:
    def __init__(self,x):
        self.num = x
class Pool:
    def __init__(self,x,y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)
    def print_num(self):
        print('水池里面一共有%d只乌龟，%d只鱼'%(self.turtle.num,self.fish.num))
        self.turtle.aaa()
pool = Pool(1,10)
pool.print_num()
#类，类对象，实例对象:如果实例对象改变类对象中属性的值，那么属性值就会被改变，
class C:
    count = 0
a = C()
b = C()
c = C()
print(a.count)
print(b.count)
#实例化对象c的值被改变，但是其他实例化对象的值没有被改变
c.count = 100
print(c.count)
print(a.count)
print(b.count)
#改变类对象中属性的值，a,b的实例化对象的值都被改变，但是c的值没有被改变,因为c已经自己把属性值改变了
#类对象就不能改变它的值
C.count = 1000
print(a.count)
print(b.count)
print(c.count)
"""
注意：
    不要试图在一个类里面定义出所有能想到的特性和方法，应该利用继承和组合机制来进行扩展
    用不同的词性命名，如属性名用名词，方法名用动词，
"""
class D:
    def x(self):
        print('哈哈哈哈')
d = D()
d.x()
#这样会使类中的方法被属性名覆盖
#d.x = 1
