def ds(x):
    return 2 * x +1
ds(5)
#使用lambda改造上述函数变为匿名函数
print(lambda x: 2 * x + 1)
g = lambda x:2 * x + 1
print(g(5))
#
def add(x,y):
    print(x+y)
add(3,4)
z = lambda x,y:x+y
print(z(3,4))
"""
lambda的作用：
    1，python写一些执行脚本时，使用lambda就可以省下定义函数的过程，比如我们只需要写一个简单的脚本来
    管理服务器时间，我们就不需要专门定义一个函数然后再调用，使用lambda就可以使得代码更加精简
    2，对于一些比较抽象而且整个程序执行下来只需要调用一两次的函数，有时候给函数起名是比较头疼的，使用
    lambda就不需要考虑命名的问题
    3，简化代码的可读性：由于普通的函数阅读经常要调到开头def部分，使用lambda函数可以省略这些步骤
"""
#filter(a,b)：过滤器，a处可以直接写None或者一个函数名，b出写需要过滤的值
#filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
#该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，
# 最后将返回 True 的元素放到新列表中。
print(list(filter(None,[1,0,True,False])))
#以下实例中会输出奇数，即所有返回0的值都不会被输出
def odd(x):
    return x % 2
temp = range(10)
show = filter(odd,temp)
print(list(show))
print(list(filter(lambda x:x%2,range(10))))
"""
map() 会根据提供的函数对指定序列做映射。
第一个参数function以参数序列中的每一个元素调用function函数，返回包含每次function函数返回值的新列表。
map(function, iterable, ...):function -- 函数,iterable -- 一个或多个序列
"""
print(list(map(lambda x:x*2,range(10))))