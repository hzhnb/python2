import random as r
class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)
    def move(self):
        self.x -= 1
        print('我的位置是：',self.x,self.y)
class GoldFish(Fish):
    pass
class Garp(Fish):
    pass
class Salmon(Fish):
    pass
class Shark(Fish):
    def __init__(self):
        #在这里，子类重写了父类的__init__（)方法：这样父类的方法被覆盖，无法正常实现调用，解决方式如下：
        #调用未绑定的父类方法来实现对
        #Fish.__init__(self)
        #使用super方法
        super().__init__()
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('吃货的梦想就是天天有的吃')
        else:
            print('太撑了,吃不下了')
fish = Fish()
fish.move()
goldfish = GoldFish()
goldfish.move()
shark = Shark()
shark.eat()
shark.move()
#python可是实现多继承,继承的调用顺序是按照继承循序依次执行的，
class Base1:
    def fool1(self):
        print('我是fool1，我为Base代言')
class Base2:
    def fool1(self):
        print('我是fool2,我为Base2代言')
class C(Base2,Base1):
    pass
c = C()
c.fool1()
c.fool1()


