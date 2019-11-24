"""
issubclass(class,classinfo):如果class时classinfo的子类，就返回True,否则范湖False
注意： 1，非严格行检查，一个类会被认为是自己的子类
2，classinfo可以是类对象元组，只要class与其中一个候选类的子类，则返回True
"""
class A:
    pass
class B(A):
    pass
print(issubclass(B,A))
print(issubclass(B,B))
print(issubclass(B,object))
"""
isinstance(object,classinfo):
"""
#hasattr(object,name):表示对象object中是否有属性name
class C:
    def __init__(self,x=0):
        self.x = x
c = C()
print(hasattr(c,'x'))
#getattr(object,name,default):对象object中属性name的值，如果不存在，则输出defult
print(getattr(c,'x'))
print(getattr(c,'y','您所访问的字符串不存在'))
#setattr(object,name,value):给object的name属性赋值value,如果name不存在，则生成一个name并且赋值value
setattr(c,'y','fishc')
print(getattr(c,'y','您所访问的字符串不存在'))
#delattr(object,name):删除对象指定的属性，如果属性不存在，则抛出异常
