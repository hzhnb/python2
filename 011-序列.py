#list():如果不带参数，则是生成一个空列表,有参数，就是把一个可迭代对象转化为列表
b = 'I love FishC.com'
b = list(b)
print(b)
c = (1,2,3,5,8,13,21,34)
print(c)
#tuple([iterable]):把一个可迭代对象转换为元组，
d = (1,2,'kkk')
print('111')
print(d)
#len(sub):返回sub的长度
print(len(b))
mem = [1,2,3,4,5,6]
print(len(mem))
#max():返回参数或者序列的最大值
print(max('Z','b','c','d','e','f'))
#min():返回参数或者序列中的最小值
#注意：使用max()方法和min()方法里面参数的类型必须是一致的
char = '0123456'
print(min(char))
f = (1,2,3,4,5)
print(min(f))
#sum(iterable,start):求和。iterable:存放要进行求和的序列，start:可选，如果有，就是把iterable+start求和
#注意：对于sum()函数，操作的必须是数字，如果是其他类型就会报错
tuple2 = (2.2,2.2,2.6,2.5,2)
print(sum(tuple2,3))
#sorted():排序
#reversed():翻转
numbers = [12,32,14,35,56,47]
print(reversed(numbers))
print(list(reversed(numbers)))
print(sorted(numbers))
#enumerate():举例如下。
print(list(enumerate(numbers)))
#zip：举例如下：g中多余的元素直接省略
g = [1,2,3,4,5,6,7,8]
h = [4,5,6,7,8]
print(list(zip(g,h)))



