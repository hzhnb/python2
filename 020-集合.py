#集合里面的所有元素都是唯一的，它具有唯一性，集合是无序的
num1 = {1,2,3,4,1,2,3}
print(num1)
"""
创建集合的两种方式：
1，把一堆元素用花括号括起来
2，使用set（）工厂函数
"""
set1 = set([1,2,3,4,2,3,1])
print(set1)
"""
如何访问集合里面的值：
1，可是使用for把集合中的数据一个个读取出来
2，可以使用in和not in判断一个元素是否在集合中 
"""
print(1 in num1)
#add()方法:添加元素
num1.add(5)
print(num1)
#remove():移除集合中一个元素
num1.remove(5)
print(num1)
#frozenset（）：创建一个不可变的集合
num2 = frozenset([1,2,3,4])
