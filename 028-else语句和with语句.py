"""
else语句：
1，if:else
2,和while一切使用 如果使用了break跳出循环，那么else语句就不会执行
3，和异常处理一起使用

"""
#以下语句如果执行了except语句，那么else语句就不会执行，否则就会在最后执行else里面的语句
try:
    int('abc')
except ValueError as reason:
    print('出错了'+str(reason))
else:
    print('没有任何异常')
i = 5
#else语句和while语句一样，如果没有break,那么会在循环的最后执行else语句
while(i>0):
    print('他的值为：',i)
    i -= 1
else:
    print('我就想蹭蹭')

#with语句：会在何时的时候自动关闭文件
#不适用wuith()语句代码如下：
f = open('c:\mytest.txt')
try:
    data = f.read()
finally:
    f.close()
#使用with()语句的代码如下：
with open(r'c:\test.txt', 'r') as f:
     data = f.read()
