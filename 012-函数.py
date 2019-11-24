"""
函数的创建过程：
    def 函数名（）：
        执行语句
如果想要设置返回值，只需要用return关键字加要返回内容就可以了
"""
def MyFirstFunction():
    print('这是我创建的第一个函数！')
    print('我表示很激动！')
    print('在此我要感谢TVB,感谢阿里巴巴，感谢马云')
MyFirstFunction()
def MySecondFunction(name):
    print(name + '我爱你！')
MySecondFunction('马云')
MySecondFunction('马化腾')
def add(num1,num2):
    result = num1 + num2
    print(result)
add(1,2)
def add1(num1,num2):
    return num1+num2
print(add1(1,2))