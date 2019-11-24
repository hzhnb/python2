#函数文档
def MyFirstFunction(name):
    '函数定义过程中的name函数'
    #因为他知识一个形式，表示占据一个位置
    print('传递过来的是'+name+'叫做实际参数')
MyFirstFunction('韩志恒')
#以下方法可以打印函数的文档
print(MyFirstFunction.__doc__)
print(help(MyFirstFunction))
print('22222')
#关键字参数,如下所示：直接在传递形参的时候给所对应的元素赋值
def SaySome(name,words):
    print(name + '->' + words)
SaySome('韩志恒','改变世界')
SaySome(words='改变世界',name='韩志恒')
#默认参数：
def SaySome1(name='马云',words='让天下没有难做的生意'):
    print(name + '->' + words)
SaySome1('韩志恒')
SaySome1('乔布斯','活着就为改变世界')
#收集参数
def SaySome2(*params,esp):
    print('参数的长度是：', len(params),esp)
    print('第二个参数是：',params[1])
SaySome2(1,2,'韩志恒','就是',esp=8)
def SaySome3(*params):
    print('参数的长度是：', len(params))
    print('第二个参数是：',params[1])
SaySome3(1,2,'韩志恒','就是')
