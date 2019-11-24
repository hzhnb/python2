#dict.fromkeys[s,v]:s:键，v:对应的值，如果不写，默认为空
dict1 = {}
print(dict1.fromkeys((1,2,3)))
print(dict1.fromkeys((1,2,3),'Number'))
print(dict1.fromkeys(((1,'one'),(2,'two'),(3,'three'))))
print(dict1.fromkeys((1,2,3),('one','two','three')))
#如果调用fromkeys不会对字典的值进行修改，会直接创建一个新的字典
print(dict1.fromkeys((1,3),'数学'))
#keys():返回所有的键，一般和for一起使用
dict1 = dict1.fromkeys((1,2,3),'赞')
print(dict1.keys())
for each in dict1.keys():
    print(each)
#values():返回所有的value值
for eachValue in dict1.values():
    print(eachValue)
#items():返回所有的键值对
for eachItem in dict1.items():
    print(eachItem)
#get（a,b）:查询a(key)对应的value，b：如果不写，那么查找到不存在的key就会输出None。如果b的值存在，那么
#当查找的key不存在的时候，就会输出b的值
print(dict1.get(1))
print(dict1.get(10,'Number'))
#clear():清空一个字典
print(dict1.clear())
"""
清空字典，也可以使用：dict1={},但是这样使用是有问题的。
a = {'姓名','韩志恒'};b=a;a={}
如果使用{}此时a已经变成空的，但是b没有清空。如果使用clear()就会将所有的都清空
"""
#copy():对字典进行拷贝，但是和直接的c=a是不一样的，这样c和a的地址是一样的，但是下面的b是另外开辟的内存空间
a = {1:'one',2:'two',3:'three'}
b = a.copy()
print(b)
#pop():将key对应的键值对移除，并返回key对应的value
print(a.pop(3))
print(a)
#popitem()：随即移除一个键值对并返回这对键值对
print(a.popitem())
print(a)
#setdefault(a,b):如果只写a,就是查找a对应的value的值，如果没有的话，就会在此字典中赋值：’a':None
#如果有b,则查找对应键值对，如果不存在，则直接添加
print(a.setdefault(1))
a.setdefault('小白')
print(a)
a.setdefault('小黑','aaa')
print(a)
#update():对字典中相对应的键值对进行修改，如果不存在，则直接赋值
b = {'小1':'狗'}
a.update(b)
print(a)