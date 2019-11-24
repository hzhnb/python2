#如果在函数中修改了全局变量，如果确实想要让他修改的话，那么就使用g“lobal”关键字修饰
count  = 5
def MyFun():
    global count
    count = 10
    print(10)
MyFun()
print(count)
#内嵌函数：在函数内部在创建一个函数
#内嵌函数只能由外部函数调用，在其他地方是无法调用的
def fun1():
    print('fun1正在被调用！')
    def fun2():
        print('fun2正在被调用!')
    fun2()
fun1()
#闭包：在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，并且外函数的返回值是内函数的引用。这样就构成了一个闭包。
def FunX(x):
    def FunY(y):
        return x * y
    return FunY
i = FunX(8)
print('333333')
print(i)
print(i(5))
print(FunX(5)(8))
#以下代码执行过程中会报错，因为内嵌函数直接修改了外部函数的变量
"""
def Fun1():
    x = 5
    def Fun2():
        x *= x
        return x
    return Fun2()
"""
#以下是对之前错误（在内嵌函数中修改外部函数的变量）的更改
def Fun1():
    x = [5]
    def Fun2():
        x[0] *= x[0]
        return x[0]
    return Fun2()
print(Fun1())
#以下是方法2：使用nonlocal关键字可以直接在内嵌函数中修改外部函数变量的值
def Fun3():
    x = 5
    def Fun4():
        nonlocal x
        x *= x
        return x
    return Fun4()
print(Fun3())
def Fun5():
    x = 5
    def Fun6():
        y  = x * x
        return y
    return Fun6
print(Fun5()())